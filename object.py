from tdw.controller import Controller
from tdw.tdw_utils import TDWUtils
from tdw.add_ons.third_person_camera import ThirdPersonCamera

c = Controller()

# Generate a unique object ID.
object_id = c.get_unique_id()
# Add a camera and look at the object (we haven't added the object yet but this will execute after adding the object).
cam = ThirdPersonCamera(position={"x": 2, "y": 1.6, "z": -1},
                        look_at=object_id)
c.add_ons.append(cam)
# Create the scene and add the object.
# Change the URL to your operating system: windows, osx, or linux.
c.communicate([TDWUtils.create_empty_room(20, 20),
               {"$type": "add_object",
                "name": "iron_box",
                "url": "https://tdw-public.s3.amazonaws.com/models/windows/2018-2019.1/iron_box",
                "scale_factor": 1.0,
                "position": {"x": 1, "y": 0, "z": -0.5},
                "rotation": {"x": 0, "y": 0, "z": 0},
                "category": "box",
                "id": object_id}])