import bpy
import os
import sys


class RBT_Render_Pass(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "lighting.render_pass"
    bl_label = "Render Pass"
    bl_option = {'REGISTER', 'UNDO'}
    
    #@classmethod
    #def poll(cls, context):
    #    return context.active_object is not None
    
    #.. final function operator
    def execute(self, context):
             
        ###/// setting AO
        def Scene_AO():
            
            bpy.data.scenes["AO"].render.engine = 'CYCLES'
            bpy.data.scenes["AO"].cycles.feature_set = 'SUPPORTED'
            bpy.data.scenes["AO"].cycles.device = 'GPU'
            bpy.data.scenes["AO"].cycles.progressive = 'PATH' 
            bpy.data.scenes["AO"].cycles.samples = 128
            bpy.data.scenes["AO"].cycles.preview_samples = 64
            bpy.data.scenes["AO"].cycles.use_adaptive_sampling = True
            bpy.data.scenes["AO"].cycles.adaptive_threshold = 0.01
            bpy.data.scenes["AO"].cycles.adaptive_min_samples = 64
            bpy.data.scenes["AO"].render.use_simplify = True
            bpy.data.scenes["AO"].display_settings.display_device = 'sRGB'
            bpy.data.scenes["AO"].view_settings.view_transform = 'Standard'
            bpy.data.scenes["AO"].view_settings.look = 'None'
            bpy.data.scenes["AO"].view_settings.exposure = 0
            bpy.data.scenes["AO"].view_settings.gamma = 1
            bpy.data.scenes["AO"].sequencer_colorspace_settings.name = 'sRGB'
            bpy.data.scenes["AO"].render.resolution_x = 1920
            bpy.data.scenes["AO"].render.resolution_y = 1080
            bpy.data.scenes["AO"].render.resolution_percentage = 100
            bpy.data.scenes["AO"].render.pixel_aspect_x = 1
            bpy.data.scenes["AO"].render.pixel_aspect_y = 1
            bpy.data.scenes["AO"].frame_start = 1
            bpy.data.scenes["AO"].frame_end = 1
            bpy.data.scenes["AO"].frame_step = 1
            bpy.data.scenes["AO"].render.fps = 25
            bpy.data.scenes["AO"].render.fps_base = 1
            bpy.data.scenes["AO"].render.use_stamp_date = True
            bpy.data.scenes["AO"].render.use_stamp_time = True
            bpy.data.scenes["AO"].render.use_stamp_render_time = True
            bpy.data.scenes["AO"].render.use_stamp_frame = True
            bpy.data.scenes["AO"].render.use_stamp_lens = True
            bpy.data.scenes["AO"].render.use_stamp_camera = True
            bpy.data.scenes["AO"].render.use_stamp_scene = True
            bpy.data.scenes["AO"].render.use_stamp_filename = True
            bpy.data.scenes["AO"].view_layers["AO"].use = True
            
            #data
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_combined = True
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_z = False
            bpy.data.scenes["AO"].view_layers["AO"].pass_alpha_threshold = 0.5
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_ambient_occlusion = True
            bpy.data.scenes["AO"].view_layers["AO"].pass_cryptomatte_depth = 6
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_cryptomatte_accurate = True
            
            #filter
            bpy.data.scenes["AO"].view_layers["AO"].use_solid = True
            bpy.data.scenes["AO"].view_layers["AO"].use_volumes = True
            bpy.data.scenes["AO"].view_layers["AO"].use_sky = False
            bpy.data.scenes["AO"].view_layers["AO"].use_ao = False
            bpy.data.scenes["AO"].view_layers["AO"].use_strand = False
        
        
        
        ###/// setting BG
        def Scene_BG():
            
            bpy.data.scenes["BG"].render.engine = 'CYCLES'
            bpy.data.scenes["BG"].cycles.feature_set = 'SUPPORTED'
            bpy.data.scenes["BG"].cycles.device = 'GPU'
            
            #Sampling
            bpy.data.scenes["BG"].cycles.progressive = 'PATH'
            bpy.data.scenes["BG"].cycles.samples = 128
            bpy.data.scenes["BG"].cycles.preview_samples = 34
            
            #Adaptive Sampling 
            bpy.data.scenes["BG"].cycles.use_adaptive_sampling = True
            bpy.data.scenes["BG"].cycles.adaptive_threshold = 0.01
            bpy.data.scenes["BG"].cycles.adaptive_min_samples = 0
            
            #Simplify
            bpy.data.scenes["BG"].render.use_simplify = True
            bpy.data.scenes["BG"].render.simplify_subdivision_render = 6
            bpy.data.scenes["BG"].render.simplify_child_particles_render = 1
            bpy.data.scenes["BG"].cycles.texture_limit_render = 'OFF'
            
            #Transparent
            bpy.data.scenes["BG"].render.film_transparent = True
            bpy.data.scenes["BG"].cycles.film_transparent_glass = True
            bpy.data.scenes["BG"].cycles.film_transparent_roughness = 0.1
            
            #Color Management
            bpy.data.scenes["BG"].display_settings.display_device = 'sRGB'
            bpy.data.scenes["BG"].view_settings.view_transform = 'Standard'
            bpy.data.scenes["BG"].view_settings.look = 'None'
            bpy.data.scenes["BG"].view_settings.exposure = 0
            bpy.data.scenes["BG"].view_settings.gamma = 1
            bpy.data.scenes["BG"].sequencer_colorspace_settings.name = 'sRGB'
            
            #Output
            bpy.data.scenes["BG"].render.image_settings.color_mode = 'RGB'
            bpy.data.scenes["BG"].render.use_placeholder = True
            bpy.data.scenes["BG"].render.image_settings.color_depth = '8'
            
            #Metadata
            bpy.data.scenes["BG"].render.use_stamp_date = True
            bpy.data.scenes["BG"].render.use_stamp_time = True
            bpy.data.scenes["BG"].render.use_stamp_render_time = True
            bpy.data.scenes["BG"].render.use_stamp_frame = True
            bpy.data.scenes["BG"].render.use_stamp_camera = True
            bpy.data.scenes["BG"].render.use_stamp_lens = True
            bpy.data.scenes["BG"].render.use_stamp_scene = True
            bpy.data.scenes["BG"].render.use_stamp_filename = True
            
            #Post Processing 
            bpy.data.scenes["BG"].render.use_compositing = True
            bpy.data.scenes["BG"].render.use_sequencer = True
            bpy.data.scenes["BG"].render.dither_intensity = 1
            
            #View layer 
            bpy.data.scenes["BG"].view_layers["B"].use = True
            
            #View layer data
            bpy.data.scenes["BG"].view_layers["B"].use_pass_combined = True
            bpy.data.scenes["BG"].view_layers["B"].cycles.denoising_store_passes = True
            bpy.data.scenes["BG"].view_layers["B"].pass_alpha_threshold = 0.5
            
            #View layer filter 
            bpy.data.scenes["BG"].view_layers["B"].use_sky = True
            bpy.data.scenes["BG"].view_layers["B"].use_ao = True
            bpy.data.scenes["BG"].view_layers["B"].use_ao = True
            bpy.data.scenes["BG"].view_layers["B"].use_strand = True
            bpy.data.scenes["BG"].view_layers["B"].use_volumes = True
        
        
        
        ###/// setting MAIN
        def Scene_MAIN():

            ## Render Properties MAIN
            bpy.data.scenes["MAIN"].render.engine = 'CYCLES'
            bpy.data.scenes["MAIN"].cycles.device = 'GPU'

            # Adaptive sampling
            bpy.data.scenes["MAIN"].cycles.use_adaptive_sampling = True
            bpy.data.scenes["MAIN"].cycles.adaptive_threshold = 0.01
            bpy.data.scenes["MAIN"].cycles.adaptive_min_samples = 64

            # Denoising viewport
            bpy.data.scenes["MAIN"].cycles.preview_denoiser = 'OPTIX'

            # Simplify
            bpy.data.scenes["MAIN"].render.use_simplify = True

            # Film
            bpy.data.scenes["MAIN"].render.film_transparent = True
            bpy.data.scenes["MAIN"].cycles.film_transparent_glass = True
            bpy.data.scenes["MAIN"].cycles.film_transparent_roughness = 0.10

            # Color Management
            bpy.data.scenes["MAIN"].view_settings.view_transform = 'Standard'

            ## Output Properties Main
            # Dimensions
            bpy.data.scenes["MAIN"].frame_end = 1
            bpy.data.scenes["MAIN"].render.fps = 25

            # Metadata
            bpy.data.scenes["MAIN"].render.use_stamp_lens = True

            ## View Layer Properties Main
            # Data
            bpy.data.scenes["MAIN"].view_layers["M"].use_pass_z = False
            bpy.data.scenes["MAIN"].view_layers["M"].cycles.denoising_store_passes = True
        
        
        
        ###/// setting SH
        def Scene_SH():
            
             bpy.data.scenes["SH"].render.engine = 'CYCLES'
             bpy.data.scenes["SH"].cycles.device = 'GPU'
             bpy.data.scenes["SH"].cycles.progressive = 'PATH' 
             bpy.data.scenes["SH"].cycles.samples = 128
             bpy.data.scenes["SH"].cycles.preview_samples = 64
             bpy.data.scenes["SH"].cycles.use_adaptive_sampling = True
             bpy.data.scenes["SH"].cycles.adaptive_threshold = 0.01
             bpy.data.scenes["SH"].cycles.adaptive_min_samples = 64
             bpy.data.scenes["SH"].render.use_simplify = True
             bpy.data.scenes["SH"].display_settings.display_device = 'sRGB'
             bpy.data.scenes["SH"].view_settings.view_transform = 'Standard'
             bpy.data.scenes["SH"].view_settings.look = 'None'
             bpy.data.scenes["SH"].view_settings.exposure = 0
             bpy.data.scenes["SH"].view_settings.gamma = 1
             bpy.data.scenes["SH"].sequencer_colorspace_settings.name = 'sRGB'
             bpy.data.scenes["SH"].render.resolution_x = 1920
             bpy.data.scenes["SH"].render.resolution_y = 1080
             bpy.data.scenes["SH"].render.resolution_percentage = 100
             bpy.data.scenes["SH"].render.pixel_aspect_x = 1
             bpy.data.scenes["SH"].render.pixel_aspect_y = 1
             bpy.data.scenes["SH"].frame_start = 1
             bpy.data.scenes["SH"].frame_end = 1
             bpy.data.scenes["SH"].frame_step = 1
             bpy.data.scenes["SH"].render.fps = 25
             bpy.data.scenes["SH"].render.fps_base = 1
             bpy.data.scenes["SH"].render.use_stamp_date = True
             bpy.data.scenes["SH"].render.use_stamp_time = True
             bpy.data.scenes["SH"].render.use_stamp_render_time = True
             bpy.data.scenes["SH"].render.use_stamp_frame = True
             bpy.data.scenes["SH"].render.use_stamp_lens = True
             bpy.data.scenes["SH"].render.use_stamp_camera = True
             bpy.data.scenes["SH"].render.use_stamp_scene = True
             bpy.data.scenes["SH"].render.use_stamp_filename = True
             bpy.data.scenes["SH"].view_layers["SD"].pass_alpha_threshold = 0.5
             bpy.data.scenes["SH"].view_layers["SD"].use_pass_ambient_occlusion = True
             bpy.data.scenes["SH"].view_layers["SD"].pass_cryptomatte_depth = 6
             bpy.data.scenes["SH"].view_layers["SD"].use_pass_cryptomatte_accurate = True
             bpy.data.scenes["SH"].view_layers["SD"].use_solid = True
             bpy.data.scenes["SH"].view_layers["SD"].use_volumes = True
             bpy.data.scenes["SH"].view_layers["SD"].use = True
        
        
        
        ###/// setting UT
        def Scene_UT():
            
            #RENDER ENGINE
            bpy.data.scenes["UT"].render.engine = 'CYCLES'
            
            #FEATURE SET
            bpy.data.scenes["UT"].cycles.feature_set = 'SUPPORTED'
            
            #DEVICE
            bpy.data.scenes["UT"].cycles.device = 'CPU'
            
            #SAMPLING
            bpy.data.scenes["UT"].cycles.samples = 128
            bpy.data.scenes["UT"].cycles.preview_samples = 32
            
            #SIMPLIFY
            bpy.data.scenes["UT"].render.use_simplify = True
            bpy.data.scenes["UT"].render.simplify_subdivision_render = 6
            bpy.data.scenes["UT"].render.simplify_child_particles_render = 1
            bpy.data.scenes["UT"].cycles.texture_limit_render = '128'
            
            #FILM
            bpy.data.scenes["UT"].cycles.film_exposure = 1
            bpy.data.scenes["UT"].cycles.pixel_filter_type = 'BLACKMAN_HARRIS'
            bpy.data.scenes["UT"].cycles.filter_width = 1.5
            bpy.data.scenes["UT"].render.film_transparent = True
            bpy.data.scenes["UT"].cycles.film_transparent_glass = True
            bpy.data.scenes["UT"].cycles.film_transparent_roughness = 0.1
            
            #COLOR MANAGEMENT
            bpy.data.scenes["UT"].display_settings.display_device = 'sRGB'
            bpy.data.scenes["UT"].view_settings.view_transform = 'Standard'
            bpy.data.scenes["UT"].view_settings.look = 'None'
            bpy.data.scenes["UT"].view_settings.exposure = 0
            bpy.data.scenes["UT"].view_settings.gamma = 1
            bpy.data.scenes["UT"].sequencer_colorspace_settings.name = 'sRGB'
            
            #DIMENSION
            bpy.data.scenes["UT"].render.resolution_percentage = 100
            
            #OUTPUT
            bpy.data.scenes["UT"].render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
            bpy.data.scenes["UT"].render.image_settings.color_depth = '16'
            
            #METADATA
            bpy.data.scenes["UT"].render.use_stamp_date = True
            bpy.data.scenes["UT"].render.use_stamp_time = True
            bpy.data.scenes["UT"].render.use_stamp_render_time = True
            bpy.data.scenes["UT"].render.use_stamp_frame = True
            bpy.data.scenes["UT"].render.use_stamp_frame_range = False
            bpy.data.scenes["UT"].render.use_stamp_memory = False
            bpy.data.scenes["UT"].render.use_stamp_hostname = False
            bpy.data.scenes["UT"].render.use_stamp_camera = True
            bpy.data.scenes["UT"].render.use_stamp_lens = True
            bpy.data.scenes["UT"].render.use_stamp_scene = True
            bpy.data.scenes["UT"].render.use_stamp_marker = False
            
            #PASSED/DATA
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_combined = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_z = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_mist = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_normal = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_vector = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_uv = False
            
            #PASSED/LIGHT
            #DIFFUSE
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_diffuse_color = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_diffuse_indirect = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_diffuse_direct = True
            #GLOSSY
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_glossy_color = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_indirect = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_glossy_direct = True
            
            #TRANSMISSION
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_color = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_indirect = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_direct = True 
            
            #VOLUME
            bpy.data.scenes["UT"].view_layers["CR"].cycles.use_pass_volume_direct = True
            bpy.data.scenes["UT"].view_layers["CR"].cycles.use_pass_volume_indirect = True
            
            #OTHER
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_ambient_occlusion = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_shadow = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_emit = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_environment = False 
        
            #PASSED/CRYPTOMATTE
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_object = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_material = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_asset = True
            bpy.data.scenes["UT"].view_layers["CR"].pass_cryptomatte_depth = 6
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_accurate = True
            
            #PASSED/FILTER
            bpy.data.scenes["UT"].view_layers["CR"].use_ao = False
            bpy.data.scenes["UT"].view_layers["CR"].use_sky = False
            bpy.data.scenes["UT"].view_layers["CR"].use_solid = True
            bpy.data.scenes["UT"].view_layers["CR"].use_strand = False
            bpy.data.scenes["UT"].view_layers["CR"].use_volumes = True
            
            #PASSED/CRYPTOMATTE
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_cryptomatte_object = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_cryptomatte_material = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_cryptomatte_asset = True
            bpy.data.scenes["UT"].view_layers["UT"].pass_cryptomatte_depth = 6
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_cryptomatte_accurate = True
            
            #PASSED/DATA
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_combined = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_z = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_mist = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_normal = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_vector = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_uv = True
            
            #PASSED/FILTER
            bpy.data.scenes["UT"].view_layers["UT"].use_ao = False
            bpy.data.scenes["UT"].view_layers["UT"].use_sky = False
            bpy.data.scenes["UT"].view_layers["UT"].use_solid = True
            bpy.data.scenes["UT"].view_layers["UT"].use_strand = False
            bpy.data.scenes["UT"].view_layers["UT"].use_volumes = True
        
        
        
        ###/// create material AO
        def Material_AO( material_name, AOCO, TextScript_Name ):
            
            AO = bpy.data.materials.new(name=material_name)
            AO.use_nodes = True
            
            AO.node_tree.nodes.remove( AO.node_tree.nodes.get('Principled BSDF') )
            
            #Getter
            Material_Output = AO.node_tree.nodes.get('Material Output')
            #Setter
            Material_Output.location = (400,30)
            
            #script
            script = AO.node_tree.nodes.new( "ShaderNodeScript" )
            script.location = (0,20)
            
            #setter script
            if AOCO == "AO" :
                # assign text script and set node AO
                bpy.data.materials[material_name].node_tree.nodes["Script"].script = bpy.data.texts[TextScript_Name]
                script.inputs[1].default_value = 100
            elif AOCO == "CO" :
                # assign text script and set node CO
                bpy.data.materials[material_name].node_tree.nodes["Script"].script = bpy.data.texts[TextScript_Name]
                script.inputs[1].default_value = 5
            
            script.inputs[5].default_value = 1
            
            #Emission
            emission = AO.node_tree.nodes.new( "ShaderNodeEmission" )
            emission.location = (200,30)
            
            AO.node_tree.links.new(script.outputs[0], emission.inputs[0])
            AO.node_tree.links.new(emission.outputs[0], Material_Output.inputs[0])
            
            return AO
        
        
        
        ###/// create material UT
        def Material_UT( material_name ):

            #buat UT material
            UT = bpy.data.materials.new(name=material_name)
            UT.use_nodes = True
            UT.node_tree.nodes.remove( UT.node_tree.nodes.get('Principled BSDF') )
            UT.node_tree.nodes.remove( UT.node_tree.nodes.get('Material Output') )
            
            #geometry
            geometry = UT.node_tree.nodes.new( "ShaderNodeNewGeometry" )
            
            #separate_xyz
            separate_xyz = UT.node_tree.nodes.new( "ShaderNodeSeparateXYZ" )
            separate_xyz.location = (250,0)
            
            #combine xyz
            combine_xyz = UT.node_tree.nodes.new( "ShaderNodeCombineXYZ" )
            combine_xyz.location = (490,0)
            
            #emission
            emission = UT.node_tree.nodes.new( "ShaderNodeEmission" )
            emission.location = (750,0)
            
            #material output
            material_output = UT.node_tree.nodes.new("ShaderNodeOutputMaterial")
            material_output.location = (980,0)
            
            #geometry ---> separate_xyz
            UT.node_tree.links.new(geometry.outputs[0], separate_xyz.inputs[0])
            
            #separate_xyz ---> combine_xyz
            UT.node_tree.links.new(separate_xyz.outputs[0], combine_xyz.inputs[0])
            UT.node_tree.links.new(separate_xyz.outputs[1], combine_xyz.inputs[2])
            UT.node_tree.links.new(separate_xyz.outputs[2], combine_xyz.inputs[1])
            
            #combine_xyz ---> emission
            UT.node_tree.links.new(combine_xyz.outputs[0], emission.inputs[0])
            UT.node_tree.links.new(emission.outputs[0], material_output.inputs[0])
            
            return UT
        
        
        
        ###/// create material SH 
        def Material_SH( material_name ):

            #buat UT material
            SH = bpy.data.materials.new(name=material_name)
            SH.use_nodes = True
            
            Principal = SH.node_tree.nodes.get('Principled BSDF')
            Principal.inputs[5].default_value = 0
            Principal.inputs[7].default_value = 1
            Principal.inputs[11].default_value = 0
            
            return SH
        
        
        
        ###/// get children collection
        def collection_Children( col, colTarget, colPathDict, calPathPrntDict ) :
            
            children_col = col
            child = col.children
            if len( child ) > 0 :
                for chd in child :
                    if chd.name == colTarget :
                        
                        # add collection path children to dictionary
                        colPathDict[chd.name] = chd
                        calPathPrntDict[chd.name] = children_col
                        break
                    
                    else :
                        collection_Children( chd, colTarget, colPathDict, calPathPrntDict )
        
        
        
        ###/// exclude layer collection
        def collection_Exclude( viewLayer, layerCollection, EXCLUDE=True ) :
            
            # get collection exclude
            layerCollection = [LC.replace("_EXCLUDE", "") for LC in layerCollection if LC.endswith("EXCLUDE")]
            
            # get path collection
            collPath_Dictionary = {} # dictionary collection path
            collPathParent_Dictionary = {} # dictionary collection parent path
            children_col = viewLayer.layer_collection.children
            for LC in layerCollection :
                if len(children_col) > 0 :
                    for exclude in children_col :
                         collection_Children( exclude, LC, collPath_Dictionary, collPathParent_Dictionary )
            
            #print( self.collPath_Dictionary[layerCollection[1]] )
            #print( self.collPathParent_Dictionary[layerCollection[1]] )
            
            # make exclude layer collection
            for colls in collPath_Dictionary :
                coll_exclude = collPath_Dictionary[colls]
                if EXCLUDE :
                    coll_exclude.exclude = True
                    
                    #bpy.data.scenes['AO'].view_layers['AO'].layer_collection.children['All'].children['Dome'].exclude = True
        
        
        
        ###/// create colection
        # name collection, link path struct collection
        def createCollection( name_coll, path_coll ) :
            
            data_coll = bpy.data.collections
            if not name_coll in data_coll : 
                bpy.ops.collection.create( name=name_coll )
                path_coll.children.link( bpy.data.collections[name_coll] )
            else :
                return False
        
        
        # dummy list for get parent struct
        List_coll = []
        
        
        ###/// link collection
        # get full and parent struct target collection, create new collection
        # master collection, target to search struct, dictionary full struct target collection < full_struct[target_coll] >, dictionary parent struct target collection < parent_struct[target_coll],
        # new name collection, link new collection to full struct, link new collection to parent struvt
        def linkCollection( master_coll=None, target_coll="", full_struct={}, parent_struct={}, new_coll=None, full_link=True, parent_link=False, new_coll_path={} ) :
            
            # get path struct
            for each_coll in master_coll.children :
                if each_coll.name == target_coll :
                    full_struct[target_coll] = master_coll.children.get( each_coll.name )
                    if master_coll.name == "Master Collection" :
                        parent_struct[target_coll] = master_coll
                        List_coll.append( master_coll )
                        break
                    
                    else :
                        if not master_coll in List_coll :
                            List_coll.append( master_coll )
                        
                        parent_struct[target_coll] = List_coll[-2].children.get( List_coll[-1].name )
                    
                    break
                
                else :
                    if not master_coll in List_coll :
                        List_coll.append( master_coll )
                    
                    linkCollection( each_coll, target_coll, full_struct, parent_struct )
            
            # create new collection
            if new_coll != None :
                if full_link == True :
                    crt_coll = createCollection( new_coll, full_struct[target_coll] )
                    if crt_coll == None :
                        new_coll_path[new_coll] = full_struct[target_coll].children[new_coll]
                
                elif parent_link == True :
                    crt_coll = createCollection( new_coll, parent_struct[target_coll] )
                    if crt_coll == None :
                        new_coll_path[new_coll] = parent_struct[target_coll].children[new_coll]
        
        
        
        ###/// append lighting
        def append_Lighting():
            
            # name lighting collection
            lighting_collection = "Light"
            search_collection = "Camera"
            path_lighting = "/RBT_Lighting_Render_Scripts/RBT_Lighting_Render_Extras/LIGHT_Wakakibo.blend/Collection"
            path_lighting = os.getcwd() + path_lighting

            object_name = "LIGHT_WAKAKIBO"
            
            # dictionary list path collection
            fullPath_Coll = {}
            parentPath_Coll = {}
            lighting_Path = {}
            
            # read collection on view layer scene
            scene = bpy.context.scene
            view_layer = bpy.context.view_layer
            master_coll = bpy.data.scenes[scene.name].view_layers[view_layer.name].layer_collection
            
            path_collection = ""
            scene_coll = bpy.context.scene.collection
            list_collections = bpy.data.collections
            if not search_collection in list_collections :
                search_collection = scene_coll.children[0].name
            
            # create light collection
            linkCollection( master_coll=scene_coll, target_coll=search_collection, full_struct=fullPath_Coll, parent_struct=parentPath_Coll, new_coll=lighting_collection, full_link=False, parent_link=True, new_coll_path=lighting_Path )
            
            # get path Light collection
            for coll in list_collections :
                if coll.name == lighting_collection :
                    for getPath in master_coll.children :
                        
                        # if collection parent to master collection
                        if getPath.name == lighting_collection :
                            path_collection = getPath
                        
                        else :
                            # get full path children collection
                            collection_Children( getPath, lighting_collection, fullPath_Coll, parentPath_Coll )
                            try : path_collection = fullPath_Coll[lighting_collection]
                            except : pass
            
            #print( path_collection )
            bpy.context.view_layer.active_layer_collection = path_collection # make path_collection as active collection
            if not object_name in list_collections :
                bpy.ops.wm.append( filename=object_name, directory=path_lighting ) # append lighting collection
        
        
        
        ###/// create scene layer pass
        def create_SceneLayer( default_scene, dict_scene_layer ) :
            
            # create material
            ut = Material_UT( "UT" )
            sh = Material_SH( "SH" )
            
            scenes = bpy.data.scenes # all scenes
            list_scenes = [ scn.name for scn in scenes ]
            for scenePass in dict_scene_layer :
                if scenePass not in scenes :
                    
                    # create scene pass
                    #SP = bpy.data.scenes.new( name=scenePass ) # new scene
                    SP = default_scene.copy() # copy scene
                    SP.use_fake_user = True
                    SP.name = scenePass
                    bpy.context.window.scene = SP # switch / change scene
                    
                    # first / default view layer
                    VL = SP.view_layers[0].name = dict_scene_layer[scenePass][0][0]
                    collection_Exclude( SP.view_layers[0], [col for col in dict_scene_layer[scenePass][1][0]] )
                    
                    if scenePass == "AO":
                        Scene_AO()
                        
                        # script for node material AO
                        nameScriptAO = "SimpleAO.osl"
                        path_SimpleAO_Script = "/RBT_Lighting_Render_Scripts/RBT_Lighting_Render_Extras/SimpleAO.osl"
                        path_SimpleAO_Script = os.getcwd() + path_SimpleAO_Script
                        simpleAO_file = open(path_SimpleAO_Script, "r")
                        simpleAO_Script = simpleAO_file.read() # Get script
                        simpleAO_file.close()

                        # create simple ao script for node
                        createSimpleAO_Script = bpy.data.texts.new( nameScriptAO )
                        createSimpleAO_Script.write( simpleAO_Script )
                        
                        # create and assign material override AO
                        ao = Material_AO( "AO", "AO", createSimpleAO_Script.name )
                        SP.view_layers[0].material_override = ao
                    
                    elif scenePass == "BG" :
                        Scene_BG()
                    elif scenePass == "MAIN" :
                        Scene_MAIN()
                    elif scenePass == "SH" :
                        Scene_SH()
                        SP.view_layers[0].material_override = sh # assign mateial override SH
                        
                    #elif scenePass == "UT" :
                    #    self.Scene_UT()
                    
                    # add more view layers
                    for viewLayerPass in zip( dict_scene_layer[scenePass][0], dict_scene_layer[scenePass][1] ) : # add some view layer
                        if viewLayerPass[0] == VL :
                            continue
                        
                        # create view layer
                        VL = SP.view_layers.new( name=viewLayerPass[0] )
                        collection_Exclude( VL, [col for col in viewLayerPass[1]] )
                        
                        bpy.context.window.view_layer = VL # switch / change view layer
                        if scenePass == "AO" and viewLayerPass[0] == "CO" :
                            co = Material_AO( "CO", "CO", createSimpleAO_Script.name )
                            VL.material_override = co # assign mateial override AO
                        elif scenePass == "SH" and viewLayerPass[0] == "SH" :
                            VL.material_override = sh # assign mateial override SH
                        elif scenePass == "UT" and viewLayerPass[0] == "UT" :
                            Scene_UT()
                            VL.material_override = ut # assign mateial override UT.UT
                        
                else :
                    if scenePass == "AO" :
                        Scene_AO()
                    elif scenePass == "BG" :
                        Scene_BG()
                    elif scenePass == "MAIN" :
                        Scene_MAIN()
                    elif scenePass == "SH" :
                        Scene_SH()
                    elif scenePass == "UT" :
                        Scene_UT()
                    
                    viewLayers = bpy.data.scenes[scenePass].view_layers # all view layers
                    list_viewLayers = [ vlyr.name for vlyr in viewLayers ]
                    for viewLayerPass in zip( dict_scene_layer[ scenePass ][0], dict_scene_layer[ scenePass ][1] ) : # add some view layer
                        if viewLayerPass[0] not in list_viewLayers :
                            
                            # create view layer
                            VL = viewLayers.new( name=viewLayerPass[0] )
                            collection_Exclude( VL, [col for col in viewLayerPass[1]] )
        
        
        
        # change name scene default
        defautNameScene = "ALL"
        default_scene = bpy.context.scene
        default_scene.name = defautNameScene
        
        default_scene.render.engine = 'CYCLES'
        default_scene.cycles.feature_set = 'SUPPORTED'
        default_scene.cycles.device = 'GPU'
        
        # get outliner area
        screen_areas = bpy.context.screen.areas
        for SA in screen_areas :
            if SA.type == "OUTLINER" :
                outliner_area = SA
                break

        # another way
        #outliner_area = next(a for a in bpy.context.screen.areas if a.type == "OUTLINER")
        
        # append ligting collection
        append_Lighting()
        
        # restriction toggles
        space = outliner_area.spaces[0]
        space.show_restrict_column_enable = True  # Collection exclusion (Checkbox icon)
        space.show_restrict_column_select = True  # Selection state (Cursor icon)
        space.show_restrict_column_hide = True  # Local visibility (Eye icon)
        space.show_restrict_column_viewport = True  # Global visibility (Monitor icon)
        space.show_restrict_column_render = True  # Render visibility (Camera icon)
        space.show_restrict_column_holdout = True  # Holdout
        space.show_restrict_column_indirect_only = True  # Indirect only
        
        # dictionary scene with view layer "scene" : ( ["view layer"], ["collection exclude"] )
        
        dict_scene_layer = {
                             "AO"   : ( [ "AO", "CO" ], [ ["Dome_EXCLUDE", "Hidden_AO_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE", "Light_EXCLUDE"],
                                                          ["Dome_EXCLUDE", "Hidden_AO_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE", "Light_EXCLUDE"] ] ),
                             
                             "BG"   : ( [ "B" ], [ ["Chars_EXCLUDE", "Envi_EXCLUDE", "Props_EXCLUDE", "Floor_EXCLUDE", "FX_EXCLUDE", "Hidden_AO_EXCLUDE", "Hidden_MAIN_EXCLUDE", "Hidden_SH_EXCLUDE", "Hidden_UT_EXCLUDE", "Hidden_CRypto_EXCLUDE", "Hidden_WallAO_EXCLUDE", "Hidden_All_EXCLUDE"] ] ),
                             
                             "MAIN" : ( [ "M", "RM" ], [ ["Floor_EXCLUDE", "Hidden_MAIN_EXCLUDE", "Hidden_All_EXCLUDE"],
                                                        ["Envi_EXCLUDE", "Dome_EXCLUDE", "Floor_EXCLUDE", "Hidden_All_EXCLUDE"] ] ),
                             
                             "SH"   : ( [ "SD", "SH" ], [ ["Chars_EXCLUDE", "Envi_EXCLUDE", "Props_EXCLUDE", "Dome_EXCLUDE", "Hidden_SH_EXCLUDE", "Hidden_All_EXCLUDE"],
                                                          ["Dome_EXCLUDE", "Hidden_SH_EXCLUDE", "Hidden_All_EXCLUDE"] ] ),
                             
                             "UT"   : ( [ "CR", "UT" ], [ ["Floor_EXCLUDE", "Hidden_UT_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE", "Light_EXCLUDE"],
                                                          ["Floor_EXCLUDE", "Hidden_UT_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE", "Light_EXCLUDE"] ] )
        }
        
        create_SceneLayer( default_scene, dict_scene_layer )
        bpy.context.window.scene = default_scene
        
        # info message if this operator work well
        message = ( "Yey., Running Script Berhasil..," )
        self.report({"INFO"}, message)
        
        return {'FINISHED'}