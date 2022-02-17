import bpy


class RBT_OT_Rigging_Transfer_Weight(bpy.types.Operator):
    bl_description = "Make sure the hierarchy in the view layer is like this ('Target' at the top, 'Rig' in the middle, 'Source' at the bottom) then select in the order of the hierarchy" 
    bl_label = "Transfer Weight"
    bl_idname = 'rigging.transfer_weight_operator' 
    bl_options = {'REGISTER','UNDO'}
    
    def execute(self, context):
        
        #get list selected object upper to lower
        sel = []
        for obj in bpy.context.selected_objects:
            sel.append(obj.name)
        target = sel[0]
        armature = sel[1]
        source = sel[2]
        
        #get list collection upper to lower
        col = []
        for collection in bpy.data.collections:
            col.append(collection.name)
        col_name1 = col[0]
        col_name2 = col[1]
        
        #set select target and set active armature
        bpy.context.active_object.select_set(False)
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj
            
        #parent set armature with empty groups
        bpy.ops.object.parent_set(type='ARMATURE_NAME', xmirror=False, keep_transform=False)
        
        #set select source and set active target
        bpy.context.active_object.select_set(False)
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj
        bpy.data.objects[source].select_set(True)
        
        #transfer weight
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', layers_select_src='NAME', layers_select_dst='ALL')
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #clear select
        bpy.ops.object.select_all(action='DESELECT')
        
        #unlink object from collection and link object to collection
        bpy.data.collections[col_name1].objects.unlink(bpy.data.objects[target])
        bpy.data.collections[col_name2].objects.link(bpy.data.objects[target])
        
        return{'FINISHED'}
