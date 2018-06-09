import bpy
import numpy as np

if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("removing mesh", mesh)
    bpy.data.meshes.remove(mesh)


for i in range(10):
    mesh = bpy.data.meshes.new(name="Plane")
    ob = bpy.data.objects.new("Test" + str(i), mesh)
    ob.location = np.random.random(size = 3)
    scn = bpy.context.scene
    scn.objects.link(ob)
    scn.objects.active = ob



#/Applications/Blender/blender.app/Contents/MacOS/blender --python simple_setup.py
