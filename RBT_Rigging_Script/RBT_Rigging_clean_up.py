import bpy 

class RBT_OT_Rigging_CleanUp(bpy.types.Operator):
    bl_description = "Clean Up Your Rig!!" 
    bl_label = "Clean Up"
    bl_idname = 'rigging.cleanup_operator' 
    bl_options = {'REGISTER','UNDO'}
    
    my_text = bpy.props.StringProperty(name = "Char Name", default = "")
    
    def execute(self, context):

        char_name = self.my_text

        for col in bpy.data.collections:
            col.name = col.name + '_DEL'
            col_del_name = col.name
            
        new_col = bpy.data.collections.new(char_name + '_RIG_COL')
        new_col_name = char_name + '_RIG_COL'
        bpy.context.scene.collection.children.link(new_col)

        for rig in bpy.data.objects:
            if rig.type == 'ARMATURE':
                if char_name in rig.name:
                    rig_name = rig.name 
                    
        obj_rig = bpy.data.objects[rig_name]
        for r in obj_rig.users_collection:
            r.objects.unlink(obj_rig)         
        new_col.objects.link(bpy.data.objects[rig_name])

                    
        for mdl in bpy.data.objects[rig_name].children:
            if mdl.type == 'MESH':
                mdl_name = mdl.name

                obj_mdl = bpy.data.objects[mdl_name]
                for m in obj_mdl.users_collection:
                    m.objects.unlink(obj_mdl)        
                new_col.objects.link(bpy.data.objects[mdl_name])

        for delete_Armature in bpy.data.armatures:
            if char_name not in delete_Armature.name:
                bpy.data.armatures.remove(delete_Armature)
                
        for delete_Coll in bpy.data.collections:
            if '_DEL' in delete_Coll.name:
                bpy.data.collections.remove(delete_Coll)
        
        
        
        return{'FINISHED'}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)