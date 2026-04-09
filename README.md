# ElectroCom-Component-Detection
An electronic component classifier that uses a custom trained YOLOv8 model for live tracking and the ElectroCom dataset for training.
This project has 2 versions, one that uses software exclusively, and one that also has a 2 servo motor stand that takes coordinates from the webcam.

## Generally

- This project uses the ElectroCom dataset *(full info and report in the .ipynb file)* to train a custom yolov8 model.
- Said model is then utilized in a local .py file to detect objects directly from our webcam and draw bounding boxes over them.
- Depending on the version, this either feeds data back to our 2 servo motor stand or not.

## Version 1
- We use the ElectroCom dataset from RoboFlow (https://universe.roboflow.com/datasetsynthesis/electrocom-61), which contains 61 classes and 2100 images.
- We only use a few select classes.
- Images per class are about 50-100.
- We export 3 files: best.pt (best weights), last.pt (last epoch weights), best.onnx (what we will use for our model)

  **Training information is found in the .ipynb file.**
- LINK TO FILE: https://colab.research.google.com/drive/1e1FRskLH6LZpXtDoFnHjWZt47VjkZM1l?usp=sharing

- LINK TO WEIGHTS: https://www.mediafire.com/file/li5otja7crz4egj/best.onnx/file
  ### Example Screenshots

## Version 2
  - We follow the same process, except our detection bounding boxes coordinates is fed into arduino code that converts it to orientation angles, which in turn moves our servos.
  - We can mount a laser pointer, or anything else we please on the top servo.
   ### Wiring
  - files for the 3D printed parts can be found at(all credit to creator): https://www.printables.com/model/465433-pan-tilt-for-sg-90-servo
  

  
