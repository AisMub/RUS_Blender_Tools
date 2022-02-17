import bpy
import os
        
   
# operator link material
class RBT_Link_Material(bpy.types.Operator):
    bl_label = 'Link Material'
    bl_idname = "lighting.link_material"
    bl_option = {"REGISTER", "UNDO"}

    # execute function link material
    def execute(self, context) :
        
        # unselect all object
        bpy.ops.object.select_all(action='DESELECT')

        # list
        default_scene = bpy.context.scene
        Name_Scene = 'Shader_Scene'
        #Blend_File = 'Z:/PROJECT_SAVE/WakakiboKids/Asset/Char/Baja/Blender/WIP/Test/WKB_C_Baja_SHD_Test.blend' # guide test
        Blend_File = ''

        # get path
        filepath = bpy.data.filepath
        filepath_split = os.path.split(filepath) #list with[path, name]
        replace_path_name = filepath_split[-1].replace('RIG', 'SHD')
        Blend_File = filepath.replace( filepath_split[-1], replace_path_name )


        shader_Scene = bpy.data.scenes.new( name=Name_Scene ) # add new scene
        bpy.context.window.scene = shader_Scene # switch active scene to shader scene


        # link collection
        suffix = 'SHD'

        with bpy.data.libraries.load(Blend_File, link=True) as (data_from, data_to) :
            #data_to.collections = data_from.collections
            for colls_name in data_from.collections :
                
                # just get collection with specify suffix
                if colls_name.endswith( suffix ) :
                    data_to.collections.append( colls_name )


        # make empty collection
        link_to_name = 'Shader_Asset'
        try :
            link_to = shader_Scene.collection.children[ link_to_name ]
        except KeyError :
            link_to = bpy.data.collections.new( link_to_name )
            shader_Scene.collection.children.link( link_to )


        location_x = 0 # for instance collection
        for new_collections in data_to.collections :
            instance = bpy.data.objects.new(new_collections.name, None)
            instance.instance_type = 'COLLECTION'
            instance.instance_collection = new_collections
            
            #shader_Scene.collection.objects.link(instance)
            link_to.objects.link(instance)
            instance.location.x = location_x
            
            #print(instance)
            bpy.data.objects[instance.name].select_set(True)
            #instance.data.override_create(remap_local_usages=True)


        # make override library
        obj_collection = bpy.data.collections

        for obj_override in obj_collection :
            col_name = obj_override.name
            if col_name.endswith( suffix ) :
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[col_name].select_set(True)
                
                # select object collection
                for obj in bpy.context.selected_objects:
                    bpy.context.view_layer.objects.active = obj
                    #print(obj)
                    
                # create override library
                bpy.ops.object.make_override_library()
                bpy.ops.object.select_all(action='SELECT') # select all
                bpy.ops.object.make_links_scene(scene=default_scene.name) # default scene


        # extra list
        suffix_MSH = 'MSH'
        suffix_Shd = 'Shd'
        suffix_GRP = 'GRP'
        mesh_materials = {} # {mesh;material} dictionary list
        bpy.context.window.scene = default_scene # switch scene to default scene

        # get material link
        scene_col = bpy.context.scene.collection.objects
        for get_obj in scene_col :
            obj_name = get_obj.name
            if obj_name.endswith(suffix_Shd) or obj_name.endswith(suffix_GRP) :
                mesh_obj = get_obj.children
                for get_mesh in mesh_obj :
                    if get_mesh.type == 'MESH' :
                        get_mat = get_mesh.data.materials
                        for mat in get_mat :
                            mesh_materials.setdefault(get_mesh.name, []).append(mat)

        # replace material to original object
        object_colls = bpy.context.collection.all_objects
        for get_object in object_colls :
            object_name = get_object.name
            if object_name.endswith(suffix_MSH) :
                object_mat = get_object.data.materials
                for mat in object_mat :
                    get_mat = mesh_materials['%s.001' % object_name][0]
                    object_mat.clear()
                    object_mat.append(get_mat)


        # delete shader scene
        bpy.data.scenes.remove( bpy.data.scenes[Name_Scene])

        # delete known collection1
        known_collection1 = bpy.data.collections.get(link_to_name)
        bpy.data.collections.remove(known_collection1)

        # delete known collection1
        known_collection2 = bpy.data.collections.get(colls_name) 
        bpy.data.collections.remove(known_collection2)

        # delete object shd
        for rig in bpy.context.selected_objects:
            Rig_name = rig.name
            bpy.ops.object.select_all(action='DESELECT')
            object_to_delete = bpy.data.objects[Rig_name]
            bpy.data.objects.remove(object_to_delete, do_unlink=True)


        # save as to PRD
        filepath_PRD = bpy.data.filepath
        filepath_split_PRD = os.path.split(filepath_PRD) #list with[path, name]
        replace_path_name_PRD = filepath_split_PRD[-1].replace('RIG', 'PRD')
        Blend_File_PRD = filepath.replace( filepath_split_PRD[-1], replace_path_name_PRD )

        # save blend
        #bpy.ops.wm.save_mainfile()

        # save as
        bpy.ops.wm.save_as_mainfile(filepath=Blend_File_PRD)
        print(' ---------- Script Done ---------- ')
        
        return {'FINISHED'} # must like this