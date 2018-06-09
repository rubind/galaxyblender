import bpy

#bpy.data.objects
mesh = bpy.data.meshes.new(name="MyMesh")
ob = bpy.data.objects.new("Test", mesh)
scn = bpy.context.scene
scn.objects.link(ob)
scn.objects.active = ob


print(mesh)

# blender --python /home/me/my_script.py
