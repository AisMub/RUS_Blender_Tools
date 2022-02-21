# from wsgiref import types
import bpy
import rna_keymap_ui

bl_info = {
    "name" : "RUS_Blender_Tool",
    "author" : "Human",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

# Modul Panel
from .RBT_Tools_Panel import RBT_PT_Modelling_Panel
from .RBT_Tools_Panel import RBT_PT_Ringging_Panel
from .RBT_Tools_Panel import RBT_PT_Layout_Panel
from .RBT_Tools_Panel import RBT_PT_Animasi_Panel
from .RBT_Tools_Panel import RBT_PT_Lighting_Render_Panel
from .RBT_Tools_Panel import RBT_PT_VFX_Panel
from .RBT_Tools_Panel import RBT_PT_Compositing_Panel
from .RBT_Tools_Panel import RBT_PT_Toolkit_Panel
from .RBT_Tools_Panel import RBT_PT_Toolkit_Link_Panel
from .RBT_Tools_Panel import RBT_PT_Scale_panel
from .RBT_Tools_Panel import RBT_PT_Rigging_Remove_Panel
#=====================================================#

# Modelling Modul Operators
from .RBT_Modelling_Operator_Scripts.RBT_Modelling_Operator import MODELLING_OT_Clean_Up_Opertor
from .RBT_Modelling_Operator_Scripts.RBT_Modelling_Operator import MODELLING_OT_Blendshape_Opertor

#Lighting Modul Operators
from .RBT_Lighting_Render_Scripts.RBT_Lighting_Link_Material import RBT_Link_Material 
from .RBT_Lighting_Render_Scripts.RBT_Render_Pass import RBT_Render_Pass

# Toolkit Modul Operators
from .RBT_Toolkit_Operator.RBT_Toolkit_Link import RBT_Toolkit_MyProperties
from .RBT_Toolkit_Operator.RBT_Toolkit_Link import RBT_OT_Toolkit_Link_Override
from .RBT_Toolkit_Operator.RBT_Toolkit_Link import RBT_OT_Toolkit_Link_Proxy
from .RBT_Toolkit_Operator.RBT_Scale import RBT_Toolkit_Scale_Operator
from .RBT_Toolkit_Operator.RBT_Scale import RBT_Toolkit_Scale_Properties

#Rigging Modul Operators
from .RBT_Rigging_Script .RBT_Rigging import RBT_OT_Rigging_Transfer_Weight
from .RBT_Rigging_Script .RBT_Rigging_clean_up import RBT_OT_Rigging_CleanUp
from .RBT_Rigging_Script .RBT_Rigging_Subdivision import RBT_OT_Rigging_Add_Subdividion
from .RBT_Rigging_Script .RBT_Rigging_Remove_Tools import RBT_OT_Rigging_Remove
#=============================================================================#

classes = [
    #Class Panel
    RBT_PT_Modelling_Panel,
    RBT_PT_Ringging_Panel,
    RBT_PT_Layout_Panel,
    RBT_PT_Animasi_Panel,
    RBT_PT_Lighting_Render_Panel,
    RBT_PT_VFX_Panel,
    RBT_PT_Compositing_Panel,
    RBT_PT_Toolkit_Panel,
    RBT_PT_Toolkit_Link_Panel,
    RBT_PT_Scale_panel,
    RBT_PT_Rigging_Remove_Panel,
    

    # Class Modelling Operator 
    MODELLING_OT_Clean_Up_Opertor,
    MODELLING_OT_Blendshape_Opertor,

    # Class Lighting Operator
    RBT_Link_Material,
    RBT_Render_Pass,

    # Class Toolkit Operator
    RBT_Toolkit_MyProperties,
    RBT_OT_Toolkit_Link_Override,
    RBT_OT_Toolkit_Link_Proxy,
    RBT_Toolkit_Scale_Operator,
    RBT_Toolkit_Scale_Properties,

    #Class Rigging Operator
    RBT_OT_Rigging_Transfer_Weight,
    RBT_OT_Rigging_CleanUp,
    RBT_OT_Rigging_Add_Subdividion,
    RBT_OT_Rigging_Remove,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_path = bpy.props.StringProperty(name="File", subtype='FILE_PATH')
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= RBT_Toolkit_MyProperties)
    bpy.types.Scene.my_tool_scale = bpy.props.PointerProperty(type= RBT_Toolkit_Scale_Properties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_path
    del bpy.types.Scene.my_tool
    del bpy.types.Scene.my_tool_scale

if __name__ == "__main__":
    register()
    # unregister() 