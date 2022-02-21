import bpy      

bl_info = {
    "name": "Remove",
    "author": "km",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > Toolshelf",
    "description": "for remove some data object",
    "warning": "",
    "doc_url": "",
    "category": "Remove_Data",
}


class RBT_OT_Rigging_Remove( bpy.types.Panel ) :
    bl_label = "Remove Tools"
    bl_idname = "rigging.remove_vertex_group"
    bl_options = {'REGISTER','UNDO'}
    #bl_parent_id = isiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ke panel rigging
    
    
    def draw( self, context ) :
        layout = self.layout
        
        box = layout.box()
        row = box.row()
        row.scale_y = 1.25
        row.label( text='', icon='MOD_ARMATURE' )
        row.operator( "remove.armature" )
        
        #box = layout.box()
        row = box.row()
        row.scale_y = 1.25
        row.label( text='', icon='GROUP_VERTEX' )
        row.operator( "remove.vtx_grp" )
        
        #box = layout.box()
        row = box.row()
        row.scale_y = 1.25
        row.label( text='', icon='SHAPEKEY_DATA' )
        row.operator( "remove.shapekey_data" )
        
        #box = layout.box()
        row = box.row()
        row.scale_y = 1.25
        row.label( text='', icon='ANIM_DATA' )
        row.operator( "remove.anim_data" )
        



# remove armature
class Remove_Armature( bpy.types.Operator ) :
    """ Remove Armature Selected Objects """
    bl_label = "Remove Armature"
    bl_idname = "remove.armature"
    bl_option = { "REGISTER", "UNDO" }
    bl_desciption = ''
    
    def execute( self, context ) :
        Objects = bpy.context.selected_objects
        for obj in Objects :
            modifiers = obj.modifiers
            for mod in modifiers :
                if mod.type == 'ARMATURE' :
                    bpy.context.view_layer.objects.active = obj # for active object
                    bpy.ops.object.modifier_remove( modifier=mod.name, report=False ) # remove armature modifier
        
        return { 'FINISHED' }



# remove vertex group
class Remove_VertexGroup( bpy.types.Operator ) :
    """ Remove Vertext Group Selected Objects """
    bl_label = "Remove Vertex Group"
    bl_idname = "remove.vtx_grp"
    bl_option = { "REGISTER", "UNDO" }
    
    def execute( self, context ) :
        Objects = bpy.context.selected_objects
        for obj in Objects :
            try :
                bpy.context.view_layer.objects.active = obj # for active object
                bpy.ops.object.vertex_group_remove( all=True ) # remove all vertex group
            except :
                pass
        
        #self.report({'INFO'}, "your massage")
        return { 'FINISHED' }


# remove shape key
class Remove_ShapeKey( bpy.types.Operator ) :
    """ Remove Animation Data Selected Objects """
    bl_label = "Remove shapekey"
    bl_idname = "remove.shapekey_data"
    bl_option = { "REGISTER", "UNDO" }
    
    def execute( self, context ) :
        
        print( 'heloooo' )
        return{ "FINISHED" }


# remove anim data
class Remove_AnimData( bpy.types.Operator ) :
    """ Remove Animation Data Selected Object """
    bl_label = "Remove Anim Data"
    bl_idname = "remove.anim_data"
    bl_option = { "REGISTER", "UNDO" }
    
    def execute( self, context ) :
        
        print( 'heloooo' )
        return{ "FINISHED" }