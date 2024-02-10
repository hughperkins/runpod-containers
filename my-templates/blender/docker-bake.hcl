group "default" {
    targets = [
        "blender",
    ]
}

target "blender" {
    dockerfile = "Dockerfile"
    tags = ["hughperkins/blender"]
    contexts = {
        scripts = "../../container-template"
        proxy = "../../container-template/proxy"
        logo = "../../container-template"
    }
    args = {
        BASE_IMAGE = "nvidia/cuda:12.1.1-devel-ubuntu22.04"
        PYTHON_VERSION = "3.10"
        TORCH = "torch torchvision torchaudio"
    }
}
