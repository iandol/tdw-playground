from time import time 
from time import sleep
from tdw.controller import Controller
from tdw.tdw_utils import TDWUtils
from tdw.add_ons.third_person_camera import ThirdPersonCamera

c = Controller()
c.communicate([{"$type": "set_screen_size", "width": 1000, "height": 1000}])
cam = ThirdPersonCamera(avatar_id="a",
                        position={"x": 13, "y": 13, "z": -0.6},
                        look_at={"x": 0, "y": 0, "z": 0})
c.add_ons.append(cam)

c.communicate(TDWUtils.create_empty_room(30, 30))
# Add a bunch of sofas.
y = 0
x = 0
a = 0
for i in range(10):
    object_id = c.get_unique_id()
    t0 = time()
    c.communicate(c.get_add_object("arflex_hollywood_sofa",
                                   object_id=object_id,
                                   rotation={"x": 0, "y": a, "z": 0},
                                   position={"x": x, "y": y, "z": 0}))
    y += 1
    x += 1
    a += 10
    print(time() - t0)
    sleep(1)
sleep(2)
c.communicate({"$type": "terminate"})