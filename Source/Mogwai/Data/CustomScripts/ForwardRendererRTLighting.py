from falcor import *

def render_graph_ForwardRenderRTLighting():
    g = RenderGraph('ForwardRenderRTLighting')
    loadRenderPassLibrary('BSDFViewer.dll')
    loadRenderPassLibrary('AccumulatePass.dll')
    loadRenderPassLibrary('Antialiasing.dll')
    loadRenderPassLibrary('DepthPass.dll')
    loadRenderPassLibrary('DebugPasses.dll')
    loadRenderPassLibrary('BlitPass.dll')
    loadRenderPassLibrary('CSM.dll')
    loadRenderPassLibrary('GBuffer.dll')
    loadRenderPassLibrary('ErrorMeasurePass.dll')
    loadRenderPassLibrary('FLIPPass.dll')
    loadRenderPassLibrary('TemporalDelayPass.dll')
    loadRenderPassLibrary('PixelInspectorPass.dll')
    loadRenderPassLibrary('ForwardLightingPass.dll')
    loadRenderPassLibrary('ImageLoader.dll')
    loadRenderPassLibrary('MegakernelPathTracer.dll')
    loadRenderPassLibrary('TestPasses.dll')
    loadRenderPassLibrary('MinimalPathTracer.dll')
    loadRenderPassLibrary('OptixDenoiser.dll')
    loadRenderPassLibrary('PassLibraryTemplate.dll')
    loadRenderPassLibrary('RTAO.dll')
    loadRenderPassLibrary('RTGeometryPass.dll')
    loadRenderPassLibrary('RTLightingPass.dll')
    loadRenderPassLibrary('SceneDebugger.dll')
    loadRenderPassLibrary('SimplePostFX.dll')
    loadRenderPassLibrary('SSAO.dll')
    loadRenderPassLibrary('SkyBox.dll')
    loadRenderPassLibrary('SVGFPass.dll')
    loadRenderPassLibrary('ToneMapper.dll')
    loadRenderPassLibrary('Utils.dll')
    loadRenderPassLibrary('WhittedRayTracer.dll')
    RTLightingPass = createPass('RTLightingPass', {'minT': 9.999999747378752e-05})
    g.addPass(RTLightingPass, 'RTLightingPass')
    GBufferRT = createPass('GBufferRT', {'samplePattern': SamplePattern.Center, 'sampleCount': 16, 'useAlphaTest': True, 'adjustShadingNormals': True, 'forceCullMode': False, 'cull': CullMode.CullBack, 'texLOD': TexLODMode.Mip0, 'useTraceRayInline': False})
    g.addPass(GBufferRT, 'GBufferRT')
    ToneMapper = createPass('ToneMapper', {'useSceneMetadata': True, 'exposureCompensation': 0.0, 'autoExposure': False, 'filmSpeed': 100.0, 'whiteBalance': False, 'whitePoint': 6500.0, 'operator': ToneMapOp.Aces, 'clamp': True, 'whiteMaxLuminance': 1.0, 'whiteScale': 11.199999809265137, 'fNumber': 1.0, 'shutter': 1.0, 'exposureMode': ExposureMode.AperturePriority})
    g.addPass(ToneMapper, 'ToneMapper')
    FXAA = createPass('FXAA', {'qualitySubPix': 0.75, 'qualityEdgeThreshold': 0.16599999368190765, 'qualityEdgeThresholdMin': 0.08330000191926956, 'earlyOut': True})
    g.addPass(FXAA, 'FXAA')
    BlitPass = createPass('BlitPass', {'filter': SamplerFilter.Linear})
    g.addPass(BlitPass, 'BlitPass')
    g.addEdge('RTLightingPass.colorOut', 'ToneMapper.src')
    g.addEdge('GBufferRT.diffuseOpacity', 'RTLightingPass.diffuseMtl')
    g.addEdge('GBufferRT.posW', 'RTLightingPass.posW')
    g.addEdge('GBufferRT.normW', 'RTLightingPass.normalW')
    g.addEdge('ToneMapper.dst', 'FXAA.src')
    g.addEdge('FXAA.dst', 'BlitPass.src')
    g.markOutput('BlitPass.dst')
    return g

ForwardRenderRTLighting = render_graph_ForwardRenderRTLighting()
try: m.addGraph(ForwardRenderRTLighting)
except NameError: None
