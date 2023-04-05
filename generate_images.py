import os
import bpy
import json

RENDER_RESOLUTION = (600, 600)
RENDER_FOLDER = "/home/manus/Documents/Development/go/github.com/ubombar/monte-carlo-denoising/renders"
SCENE_JSON = "/home/manus/Documents/Development/go/github.com/ubombar/monte-carlo-denoising/gen/scenes.json"
   
def clear_scene():
    for o in bpy.context.scene.objects:
        if o.type == 'MESH':
            o.select_set(True)
        else:
            o.select_set(False)

    # Call the operator only once
    bpy.ops.object.delete()

def render_scene(scene):
    bpy.context.scene.render.resolution_x = RENDER_RESOLUTION[0]
    bpy.context.scene.render.resolution_y = RENDER_RESOLUTION[1]
    
    for cube in scene["objects"]["kubes"]:
        bpy.ops.mesh.primitive_cube_add(location=(cube["pos_x"], cube["pos_y"], cube["pos_z"]), size=cube["size"])

    for cube in scene["objects"]["spheres"]:
        bpy.ops.mesh.primitive_uv_sphere_add(location=(cube["pos_x"], cube["pos_y"], cube["pos_z"]), radius=cube["radius"])

    for cube in scene["objects"]["cones"]:
        bpy.ops.mesh.primitive_cone_add(location=(cube["pos_x"], cube["pos_y"], cube["pos_z"]), radius1=cube["radius1"], radius2=cube["radius2"])

    output_file = os.path.join(RENDER_FOLDER, f"{scene['id']}.png")

    bpy.ops.render.render(write_still=True)

    # Save the rendered output
    bpy.data.images["Render Result"].save_render(filepath=output_file)
    
    clear_scene()

if __name__ == "__main__":
    with open(SCENE_JSON, "r") as f:
        scene_list = json.load(f)
    
    for scene in scene_list:
        render_scene(scene)