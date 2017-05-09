# peoplecount-camera

Device flow for camera devices. Communicates with other devices and/or services via MQTT. The server-side code is available in [peoplecount-server](https://github.com/seansund/peoplecount-server).

The camera device is initiated via a command from the 'server' via MQTT containing the capture_id. The camera device captures an image via the camera then processes the image using OpenCV to count the number of objects in the image (people in this case). The resulting count and metadata about the image is published to a topic for processing by downstream components.
