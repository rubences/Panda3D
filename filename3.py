from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3
from math import sin, cos





class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.environ.reparentTo(self.render)

        # Scale and position the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Add a task to rotate the camera.
        self.taskMgr.add(self.spin_camera_task, "spin_camera_task")

    # Define a procedure to move the camera.
    def spin_camera_task(self, task):
        angle_degrees = task.time * 6.0
        angle_radians = angle_degrees * (3.14159 / 180.0)
        self.camera.setPos(20 * sin(angle_radians), -20 * cos(angle_radians), 3)
        self.camera.lookAt(Point3(0, 0, 0))
        return task.cont

app = MyApp()
app.run()
