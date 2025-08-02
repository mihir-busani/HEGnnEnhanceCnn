print("models/__init__.py starting")

try:
    from .gnn import (
        GINTopK4,
        GINTopK2,
        GCNTopK4,
        GCNTopK2
    )
    print("Imported gnn")
except Exception as e:
    print("Failed gnn:", e)

try:
    from .resnet import (
        resnet32,
        resnet110,
        wide_resnet20_8,
    )
    print("Imported resnet")
except Exception as e:
    print("Failed resnet:", e)

try:
    from .mlp import MLP
    print("Imported MLP")
except Exception as e:
    print("Failed MLP:", e)

try:
    gnn_model_dict = {
        'gintopk4': GINTopK4,
        'gintopk2': GINTopK2,
        'gcntopk4': GCNTopK4,
        'gcntopk2': GCNTopK2,
    }

    cnn_model_dict = {
        'resnet32': resnet32,
        'resnet110': resnet110,
        'wide_resnet20_8': wide_resnet20_8,
    }
    print("Model dicts defined")
except Exception as e:
    print("Failed defining model dicts:", e)

print("models/__init__.py done")
