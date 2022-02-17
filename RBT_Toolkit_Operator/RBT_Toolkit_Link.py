from dataclasses import replace
import bpy
import os


class RBT_Toolkit_MyProperties(bpy.types.PropertyGroup):
    
    my_numberOfObject : bpy.props.IntProperty(name= 'How Many?', soft_min= 0, soft_max= 1000, default= (1))

        
class RBT_OT_Toolkit_Link_Override(bpy.types.Operator):
    bl_description = "Link and Make Override with the file you\'ve selected"
    bl_label = "Link & Make Override Library"
    bl_idname = "toolkit.link_override"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        scn = context.scene
        mypath = scn.my_path
        
        file = mypath
        blendFile = r"%s" %file
        
        scene = context.scene
        mytool = scene.my_tool
        how_many = mytool.my_numberOfObject
        for i in range(how_many):
            context = bpy.context
            scenes = []
            Scn = bpy.context.scene
            mainCollection = bpy.data.scenes[Scn.name].collection
            with bpy.data.libraries.load(blendFile) as (data_from, data_to):
                for name in data_from.scenes:
                    scenes.append({'name': name})
                action = bpy.ops.wm.link
                #blendFile = blendFile.replace('/', '\\')
        #print( blendFile + "/Scene/" )
                action(directory=blendFile + "/Scene/", files=scenes)
                scenes = bpy.data.scenes[-len(scenes):]
            for scene in scenes:
                for coll in scene.collection.children:
                    instance = bpy.data.objects.new('Instance', None)
                    instance.instance_type = 'COLLECTION'
                    instance.instance_collection = coll
                    mainCollection.objects.link(instance)
                    # make override library
                    bpy.data.objects['Instance'].select_set(True)
                        
                    # select object collection
                    for obj in bpy.context.selected_objects:
                        bpy.context.view_layer.objects.active = obj
                        #print(obj)
                        
                    bpy.ops.object.make_override_library()
                            

                bpy.data.scenes.remove(scene)
                
            print('-----------------------SCRIPT DONE-----------------------')
        #self.report( {"INFO"}, blendFile + "/Scene/" )
        return {'FINISHED'}
    
class RBT_OT_Toolkit_Link_Proxy(bpy.types.Operator):
    bl_description = "Link and Make Proxy with the file you\'ve selected"
    bl_label = "Link & Make Proxy"
    bl_idname = "toolkit.link_proxy"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        scn = context.scene
        mypath = scn.my_path
        
        file = mypath
        blendFile = r"%s" %file
        
        context = bpy.context
        scenes = []
        Scn = bpy.context.scene
        mainCollection = bpy.data.scenes[Scn.name].collection
        with bpy.data.libraries.load(blendFile) as (data_from, data_to):
            for name in data_from.scenes:
                scenes.append({'name': name})
            action = bpy.ops.wm.link
            action(directory=blendFile + "/Scene/", files=scenes)
            scenes = bpy.data.scenes[-len(scenes):]
        for scene in scenes:
            for coll in scene.collection.children:
                ins_name = coll.name
                instance = bpy.data.objects.new(ins_name, None)
                instance.instance_type = 'COLLECTION'
                instance.instance_collection = coll
                mainCollection.objects.link(instance)
                # make override library
                bpy.data.objects[ins_name].select_set(True)
                    
                # select object collection
                for obj in bpy.context.selected_objects:
                    bpy.context.view_layer.objects.active = obj
                    #print(obj)
                    
                bpy.ops.object.proxy_make()
                        

            bpy.data.scenes.remove(scene)
            
        print('-----------------------SCRIPT DONE-----------------------')        
        
        return {'FINISHED'}    