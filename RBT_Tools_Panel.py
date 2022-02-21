import bpy

# ========== Modeling ==========#
class RBT_PT_Modelling_Panel(bpy.types.Panel):
    bl_label = "Modeling"
    bl_idname = "RBT_PT_Modelling"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        box = layout.box()
        row = box.row()
        #Clean Up operator
        row.operator('modelling.clean_up') 
        
        row.operator('modelling.extract_blends hape')


# ========== Ringging ==========#
class RBT_PT_Ringging_Panel(bpy.types.Panel):
    bl_label = "rigging"
    bl_idname = "RBT_PT_Ringging"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        row = layout.row()
        row.operator("rigging.transfer_weight_operator")
        row.operator("rigging.cleanup_operator")

        
        row = layout.row()
        row.operator("rigging.add_subdivision_operator")

    #========= class Romove==#
class RBT_OT_Rigging_Remove( bpy.types.Panel ) :
    bl_label = "Remove Tools"
    bl_idname = "rigging.remove_vertex_group"
    bl_options = {'REGISTER','UNDO'}
    bl_parent_id = "RBT_PT_Ringging"
    
    
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

# class RBT_PT_Rigging_Remove_Panel(bpy.types.Panel):
#     bl_label = "Remove"
#     bl_idname = "RBT_PT_Remove_panel"
#     bl_space_type = 'VIEW_3D'
#     bl_region_type = 'UI'
#     bl_category = "RBT"
#     

#     def draw (self, context):
#         layout = self.layout
#         layout.scale_y = 1.3
        
#         row = layout.row()
#         row.operator("rigging.remove_vertex_group")

      
# ========== Layout ==========#        
class RBT_PT_Layout_Panel(bpy.types.Panel):
    bl_label = "Layout"
    bl_idname = "RBT_PT_Layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        row = layout.row()
        #Label
        row.label(text= "Layout")
        row = layout.row()
        
# ========== Animasi ==========#
class RBT_PT_Animasi_Panel(bpy.types.Panel):
    bl_label = "Animasi"
    bl_idname = "RBT_PT_Animasi"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        row = layout.row()
        #Label
        row.label(text= "Animasi")
        row = layout.row()
        
# ========== Lighting/Rendering ==========#
class RBT_PT_Lighting_Render_Panel(bpy.types.Panel):
    bl_label = "Lighting / Rendering"
    bl_idname = "RBT_PT_Lighting_Render"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3

        box = layout.box()
        row = box.row()
        row.operator('lighting.link_material') 

        row.operator('lighting.render_pass')

        
# ========== VFX ==========#
class RBT_PT_VFX_Panel(bpy.types.Panel):
    bl_label = "VFX"
    bl_idname = "RBT_PT_VFX"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        row = layout.row()
        #Label
        row.label(text= "VFX")
        row = layout.row()
        

# ========== Compositing ==========#
class RBT_PT_Compositing_Panel(bpy.types.Panel):
    bl_label = "Compositing"
    bl_idname = "RBT_PT_Compositing"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        row = layout.row()
        #Label
        row.label(text= "Compositing")
        row = layout.row()
        
# ========== Toolkit ==========#
class RBT_PT_Toolkit_Panel(bpy.types.Panel):
    bl_label = "Toolkit"
    bl_idname = "RBT_PT_Toolkit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_option = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3

        row = layout.row()
        #Label
        row.label(text= "Toolkit")
        row = layout.row()

        #Class scale
class RBT_PT_Scale_panel(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "RBT_PT_Scale_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RBT"
    bl_parent_id = "RBT_PT_Toolkit"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool_scale
        
        # layout.prop(mytool, "my_string")
        layout.prop(mytool, "my_float_vector")
        layout.prop(mytool, "my_enum")
 
        layout.operator("toolkit.scale_freeze_operator")

        
# =========================================#

class RBT_PT_Toolkit_Link_Panel(bpy.types.Panel):
    bl_label = "Link"
    bl_idname = 'RBT_PT_Toolkit_Link_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RBT'
    bl_parent_id = 'RBT_PT_Toolkit'
    
    def draw (self, context):
        #start draw file browser        
        layout = self.layout
        scn = context.scene

        col = layout.column(align=True)
        col.prop(scn, "my_path", text="")

        # Print the absolute and relative path to the console
        print ("REL:", scn.my_path)
        print ("ABS:", bpy.path.abspath(scn.my_path))
        #end draw file browser 
        
        scene = context.scene
        mytool = scene.my_tool
        layout = self.layout
        
        box = layout.box()
        box.label(text = 'Link Override')
        box.prop(mytool, "my_numberOfObject")      
        box.operator("toolkit.link_override")
        
        box = layout.box()
        box.label(text = 'Link Proxy')    
        box.operator("toolkit.link_proxy")  
        # =====END=====#

print("hallo masyarakat")