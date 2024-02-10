# blender --background file.blend --python bake_fluid.py

import bpy

for scene in bpy.data.scenes:
    for object in scene.objects:
        for modifier in object.modifiers:
            if modifier.type == 'FLUID':
                if modifier.fluid_type == 'DOMAIN':
                    print(scene, object, object.name, modifier, 'modifier.fluid_type', modifier.fluid_type)
                    print('baking...')
                    object.select_set(True)
                    bpy.context.view_layer.objects.active = object
                    bpy.ops.fluid.bake_all()

bpy.ops.wm.save_mainfile()
