from time import sleep
from tdw.controller import Controller
from tdw.tdw_utils import TDWUtils
from tdw.add_ons.third_person_camera import ThirdPersonCamera


"""
Follow the position of an object.
"""

c = Controller()

object_id = c.get_unique_id()
object_id2 = c.get_unique_id()
# Create a third-person camera that will follow the object.
cam = ThirdPersonCamera(avatar_id="a",
                        position={"x": 1, "y": 3, "z": -0.6},
                        follow_object=object_id,
                        follow_rotate=False,
                        look_at=object_id)
c.add_ons.append(cam)
c.communicate([TDWUtils.create_empty_room(9, 9),
               c.get_add_object(model_name="iron_box",
                                library="models_core.json",
                                position={"x": 0, "y": 0, "z": 0},
                                object_id=object_id),
               {"$type": "apply_force_to_object",
                "id": object_id,
                "force": {"x": 0, "y": 20, "z": 0}},
                c.get_add_object(model_name="iron_box",
                                library="models_core.json",
                                position={"x": 1, "y": 0, "z": 1},
                                object_id=object_id2),
               {"$type": "apply_force_to_object",
                "id": object_id2,
                "force": {"x": 0, "y": 10, "z": 0}}])
sleep(2)
for i in range(1000):
    c.communicate([])
# Stop following the object.
cam.follow_object = None
sleep(2)
c.communicate({"$type": "terminate"})