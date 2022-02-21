import bpy

# rigging add subdivision
class RBT_OT_Rigging_Add_Subdividion(bpy.types.Operator) :
    
    """ Add Subdivision Selected Object _MSH """
    bl_label = "Add Subdivision"
    bl_idname = "rigging.add_subdivision_operator"
    bl_option = {'REGISTER', 'UNDO'}
    
    def execute(self, context) :
    
        # list
        properties1 = "smooth view"
        properties2 = "smooth render"
        
        context = bpy.context
        scene = context.scene
        
        # create custom properties "smooth render" scene porperties
        scene['_RNA_UI'] = scene.get('_RNA_UI', {})
        scene[properties1] = 1
        scene['_RNA_UI'][properties1] = {"name": properties1,
                                      "description": "ToolTip",
                                      "default": 0,
                                      "min": 0,
                                      "max": 6}
        
        # create custom properties "smooth view" scene properties
        scene[properties2] = 1
        scene['_RNA_UI'][properties2] = {"name": properties2,
                                      "description": "ToolTip",
                                      "default": 0,
                                      "min": 0,
                                      "max": 6}
        
        # add driver function single property
        def add_driver_object( src, prop, tgtType, tgt, tgtDataPath ):
            
            # add driver
            fCurve = src.driver_add(prop)
            driver = fCurve.driver
            driver.expression = 'var'
            
            # create a variable
            var = driver.variables.new()
            var.name = 'var'
            var.type = 'SINGLE_PROP'
            
            target = var.targets[0]
            target.id_type = tgtType
            target.id = tgt
            target.data_path = tgtDataPath
        
        # get active collection
        Col = bpy.context.collection
        
        # list selected
        #Col.selected_objects
        modifier_name = 'Subdivision'
        attr_prop1 = 'levels'
        attr_prop2 = 'render_levels'
        
        # each object in collection
        for obj in bpy.data.collections[Col.name].all_objects:
            if obj.type == 'MESH' :
                
                # just only mesh with prefix '_MSH'
                object_name = obj.name
                if object_name.split('_')[-1] == 'MSH' :
                    if modifier_name not in obj.modifiers :
                        
                        # add subdivision modifier to mesh
                        add_modif = obj.modifiers.new('Subdivision', type='SUBSURF')
                        add_modif.show_only_control_edges = True
                        
                        add_driver_object( add_modif, attr_prop1, 'SCENE', scene, '["%s"]' % properties1 )
                        add_driver_object( add_modif, attr_prop2, 'SCENE', scene, '["%s"]' % properties2 )
                    
                    # get modifiers exist
                    else :
                        for mod in obj.modifiers :
                            if mod.type == 'SUBSURF' :
                                #print(mod)
                                
                                # query if subdivision modifier already has driver connection
                                anim = obj.animation_data
                                if anim is not None :
                                    for obj_drv in anim.drivers :
                                        'print ( obj.name )'
                                        'print ( obj_drv.data_path )'
                                        'print ( obj_drv.driver.expression )'
                                        if obj_drv.data_path == attr_prop1 or obj_drv.data_path == attr_prop2 :
                                            pass
                                        
                                        else :
                                            print( "%s not connect subdivision driver" % obj.name )
                                            
                                # subdivision which has not been connected to driver 
                                else :
                                    add_driver_object( mod, attr_prop1, 'SCENE', scene, '["%s"]' % properties1 )
                                    add_driver_object( mod, attr_prop2, 'SCENE', scene, '["%s"]' % properties2 )        
                    
                    # shade smooth object
                    obj_poly = bpy.data.objects[obj.name].data.polygons
                    for smoothes in obj_poly :
                        smoothes.use_smooth = True
        
        self.report({'INFO'}, "Add Subivision success..,")
        return {"FINISHED"}