import bpy
import numpy as np
from mathutils import Vector
from bpy_extras.image_utils import load_image


def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat

def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)


def material_for_texture(fname):
    img = bpy.data.images.load(fname)

    tex = bpy.data.textures.new(fname, 'IMAGE')
    tex.image = img

    mat = bpy.data.materials.new(fname)
    mat.texture_slots.add()
    ts = mat.texture_slots[0]
    ts.texture = tex
    ts.texture_coords = 'UV'
    ts.uv_layer = 'default'

    return mat



if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("removing mesh", mesh)
    bpy.data.meshes.remove(mesh)


#scn = bpy.context.scene
"""
new_img = bpy.data.images.load("galaxy.png")
cTex = bpy.data.textures.new('ColorTex', type = 'IMAGE')
cTex.image = new_img
mat2 = bpy.data.materials.new('TexMat')
mat2.diffuse_color = cTex
"""

mat = material_for_texture("galaxy.png")
    
"""
"""

red = makeMaterial('Red', (1,0,0), (1,1,1), 1)

# obj.material_slots[0].material.node_tree.nodes["main image"].image = new_img

for i in range(10):
    #mesh = bpy.data.meshes.primative_plane_add(name="Plane")
    #ob = bpy.data.objects.new("Test" + str(i), mesh)
    #ob.location = np.random.random(size = 3)*5
    #ob.dimensions = Vector((2.0, 2.0, 0.0))
    #ob.dimensions

    mesh = bpy.ops.mesh.primitive_plane_add(location = np.random.random(size = 3)*5)
    #ob = bpy.data.objects.new("Test" + str(i), mesh)
    #mesh.materials.append(mat)

    #ob = bpy.context.active_object
    setMaterial(bpy.context.object, mat)

    #ob.material_slots[0].material.node_tree.nodes["main image"].image = new_img

    #scn.objects.link(ob)
    #scn.objects.active = ob



#/Applications/Blender/blender.app/Contents/MacOS/blender --python simple_setup.py
