import bpy


#Clean up 
class MODELLING_OT_Clean_Up_Opertor(bpy.types.Operator):
    bl_label = "Clean Up"
    bl_idname = 'modelling.clean_up'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        #clear select
        bpy.ops.object.select_all(action='DESELECT')

        #variable library
        context = bpy.context
        scene = context.scene
        object = scene.objects

        #create Empty Group
        bpy.ops.object.empty_add(type = 'PLAIN_AXES')

        #get object type 'Empty' and rename it
        for geo in object:
            if geo.type == 'EMPTY':
                geo.name = 'Geo'
                geo_name = geo.name       

        #get object type 'Mesh'
        for obj in object:
            if obj.type == 'MESH':
                #make condition must including '_MSH' as suffix
                if '_MSH' not in obj.name:
                    obj_name = obj.name + '_MSH'
                    obj.name = obj_name
                obj.select_set(True)


    

        #parent selected object(mesh) into active object(empty group)
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

        #clear select
        bpy.ops.object.select_all(action='DESELECT')
        
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA':
                 obj.select_set(True)
        
            elif obj.type == 'LIGHT':
                obj.select_set(True)
        
        bpy.ops.object.delete()
        return{'FINISHED'}

class MODELLING_OT_Blendshape_Opertor(bpy.types.Operator):
    bl_label = "Extract Blendshape"
    bl_idname = "modelling.extract_blendshape"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Hello World")

        return{'FINISHED'}