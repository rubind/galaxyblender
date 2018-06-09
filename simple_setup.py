import bpy
import numpy as np
from mathutils import Vector
from bpy_extras.image_utils import load_image


if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("removing mesh", mesh)
    bpy.data.meshes.remove(mesh)


#scn = bpy.context.scene
new_img = bpy.data.images.load("galaxy.png")
# obj.material_slots[0].material.node_tree.nodes["main image"].image = new_img

for i in range(10):
    #mesh = bpy.data.meshes.primative_plane_add(name="Plane")
    #ob = bpy.data.objects.new("Test" + str(i), mesh)
    #ob.location = np.random.random(size = 3)*5
    #ob.dimensions = Vector((2.0, 2.0, 0.0))
    #ob.dimensions

    mesh = bpy.ops.mesh.primitive_plane_add(location = np.random.random(size = 3)*5)
    #ob = bpy.data.objects.new("Test" + str(i), mesh)
    ob = bpy.context.active_object
    #ob.material_slots[0].material.node_tree.nodes["main image"].image = new_img

    #scn.objects.link(ob)
    #scn.objects.active = ob



#/Applications/Blender/blender.app/Contents/MacOS/blender --python simple_setup.py
