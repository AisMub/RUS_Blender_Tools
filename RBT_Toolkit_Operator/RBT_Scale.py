import bpy



class RBT_Toolkit_Scale_Properties(bpy.types.PropertyGroup):
    
    # my_string : bpy.props.StringProperty(name= "Enter Text")
    
    my_float_vector : bpy.props.FloatVectorProperty(name= "Scale", soft_min= 0, soft_max= 1000, default= (1,1,1))
    
    my_enum : bpy.props.EnumProperty(
        name= "Enumerator / Dropdown",
        description= "sample text",
        items= [('OP1', "All Object", ""),
                ('OP2', "Armature", ""),              
        ]
    )

class RBT_Toolkit_Scale_Operator(bpy.types.Operator):
    bl_label = "Scale & Freeze"
    bl_idname = "toolkit.scale_freeze_operator"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool_scale


        object = scene.objects
        # self.report({"INFO"}, mytool.my_enum)
        
        for obj in object:
           if mytool.my_enum == 'OP1':
                # make condition must including '_MSH' as suffix
                obj.select_set(True)
                

                obj.scale[0] = obj.scale[0] * mytool.my_float_vector[0]
                obj.scale[1] = obj.scale[1] * mytool.my_float_vector[1]
                obj.scale[2] = obj.scale[2] * mytool.my_float_vector[2]
                bpy.ops.object.transforms_to_deltas(mode='SCALE')

           elif mytool.my_enum == 'OP2':       
                if obj.type == 'ARMATURE':
                    obj.select_set(True)
                    
                    obj.scale[0] = obj.scale[0] * mytool.my_float_vector[0]
                    obj.scale[1] = obj.scale[1] * mytool.my_float_vector[1]
                    obj.scale[2] = obj.scale[2] * mytool.my_float_vector[2]
                    bpy.ops.object.transforms_to_deltas(mode='SCALE')


            
            
        # if mytool.my_enum == 'OP2':
        #     bpy.ops.mesh.primitive_uv_sphere_add()
        #     bpy.context.object.name = mytool.my_string
        #     bpy.context.object.scale[0] = mytool.my_float_vector[0]
        #     bpy.context.object.scale[1] = mytool.my_float_vector[1]
        #     bpy.context.object.scale[2] = mytool.my_float_vector[2]
            
        
        
        
        # if mytool.my_enum == 'OP3':
        #     bpy.ops.mesh.primitive_monkey_add()
        #     bpy.context.object.name = mytool.my_string
        #     bpy.context.object.scale[0] = mytool.my_float_vector[0]
        #     bpy.context.object.scale[1] = mytool.my_float_vector[1]
        #     bpy.context.object.scale[2] = mytool.my_float_vector[2]
        
        return {'FINISHED'}

'''if mytool.my_enum == 'OP1':
            bpy.ops.mesh.primitive_cube_add()
            bpy.context.object.name = mytool.my_string
            bpy.context.object.scale[0] = mytool.my_float_vector[0]
            bpy.context.object.scale[1] = mytool.my_float_vector[1]
            bpy.context.object.scale[2] = mytool.my_float_vector[2]'''