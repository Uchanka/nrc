from falcor import *

def render_graph_DefaultRenderGraph():
    g = RenderGraph('DefaultRenderGraph')
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
    loadRenderPassLibrary('RTGeometryPass.dll')
    loadRenderPassLibrary('NRCPathTracer.dll')
    loadRenderPassLibrary('OptixDenoiser.dll')
    loadRenderPassLibrary('PassLibraryTemplate.dll')
    loadRenderPassLibrary('RTAO.dll')
    loadRenderPassLibrary('RTLightingPass.dll')
    loadRenderPassLibrary('SceneDebugger.dll')
    loadRenderPassLibrary('SimplePostFX.dll')
    loadRenderPassLibrary('SSAO.dll')
    loadRenderPassLibrary('SkyBox.dll')
    loadRenderPassLibrary('SVGFPass.dll')
    loadRenderPassLibrary('ToneMapper.dll')
    loadRenderPassLibrary('Utils.dll')
    loadRenderPassLibrary('WhittedRayTracer.dll')
    ErrorMeasurePass = createPass('ErrorMeasurePass', {'ReferenceImagePath': '', 'MeasurementsFilePath': 'D:\\LittleCreator\\NeuralRadianceCache\\Outputs\\Metrics\\measure.csv', 'IgnoreBackground': True, 'ComputeSquaredDifference': True, 'ComputeAverage': True, 'UseLoadedReference': False, 'ReportRunningError': True, 'RunningErrorSigma': 0.9950000047683716, 'SelectedOutputId': OutputId.Source})
    g.addPass(ErrorMeasurePass, 'ErrorMeasurePass')
    ImageLoader = createPass('ImageLoader', {'mips': False, 'srgb': True, 'arrayIndex': 0, 'mipLevel': 0})
    g.addPass(ImageLoader, 'ImageLoader')
    ImageLoader_ = createPass('ImageLoader', {'mips': False, 'srgb': True, 'arrayIndex': 0, 'mipLevel': 0})
    g.addPass(ImageLoader_, 'ImageLoader_')
    g.addEdge('ImageLoader.dst', 'ErrorMeasurePass.Source')
    g.addEdge('ImageLoader_.dst', 'ErrorMeasurePass.Reference')
    g.markOutput('ErrorMeasurePass.Output')
    return g

DefaultRenderGraph = render_graph_DefaultRenderGraph()
try: m.addGraph(DefaultRenderGraph)
except NameError: None
