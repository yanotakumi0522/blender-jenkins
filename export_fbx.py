import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]

input_path = argv[0]
output_path = argv[1]

bpy.ops.wm.open_mainfile(filepath=input_path)

bpy.ops.export_scene.fbx(
    filepath=output_path,
    use_selection=False,
    bake_anim=True,
    add_leaf_bones=False,
    axis_forward='-Z',
    axis_up='Y'
)

print("FBX export complete")
#test1
