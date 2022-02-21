import bpy      

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