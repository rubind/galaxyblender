import bpy

mesh = bpy.data.meshes.new(name="Plane")
ob = bpy.data.objects.new("Test", mesh)
scn = bpy.context.scene
scn.objects.link(ob)
scn.objects.active = ob



#/Applications/Blender/blender.app/Contents/MacOS/blender --python simple_setup.py
