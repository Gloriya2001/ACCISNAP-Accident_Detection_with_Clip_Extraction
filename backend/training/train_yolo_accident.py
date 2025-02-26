from ultralytics import YOLO
import torch

# Check if CUDA (GPU) is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # Use yolov8s.pt or yolov8m.pt for better accuracy

# Train the model on your dataset
model.train(
    data="../dataset/dataset.yaml",  # Correct dataset path
    epochs=10,           # Increase epochs for better accuracy
    imgsz=640,            # Input image size
    batch=1,             # Adjust based on GPU memory
    lr0=0.001,            # Initial learning rate
    device=device,        # Use GPU if available
    save=True,            # Save best model checkpoints
    name="accident_yolo"  # Name of the training run
)

# Validate the trained model
metrics = model.val()
print("Model Evaluation Metrics:", metrics)

# Export the trained model to ONNX format for fast inference
print("Exporting model to ONNX format...")
model.export(format="onnx")

# Export to TensorRT for optimized inference (Optional)
print("Exporting model to TensorRT...")
model.export(format="engine")

print("✅ Training and optimization completed successfully! 🚀")
