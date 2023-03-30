import json
import random
import math

def generate_random(minimum, maximum):
    return random.random() * (maximum - minimum) - minimum

def generate_material():
    MATERIALS = ["normal", "metal", "plastic", "glass", "light"]
    return MATERIALS[random.randint(0, len(MATERIALS))]

def generate_kube(range_size: tuple[float], plane: float):
    return {
        "type": "kube",
        "pos_x": random.random() * 2 * plane - plane,
        "pos_y": random.random() * 2 * plane - plane,
        "size": generate_random(*range_size)
    }

def generate_sphere(range_radius: tuple[float], plane: float):
    return {
        "type": "sphere",
        "pos_x": random.random() * 2 * plane - plane,
        "pos_y": random.random() * 2 * plane - plane,
        "radius": generate_random(*range_radius)
    }

def generate_cone(range_radius: tuple[float], range_height: tuple[float], plane: float):
    return {
        "type": "cone",
        "pos_x": random.random() * 2 * plane - plane,
        "pos_y": random.random() * 2 * plane - plane,
        "radius": generate_random(*range_radius),
        "height": generate_random(*range_height)
    }

def generate_light(range_heigth: tuple[float], plane: float):
    return {
        "type": "cone",
        "pos_x": random.random() * 2 * plane - plane,
        "pos_y": random.random() * 2 * plane - plane,
        "pos_z": generate_random(*range_heigth)
    }

def generate_scene_object(
        id: int,
        plane: float, 
        fov: float, 
        range_heigth: tuple[float],
        range_num_kubes: tuple[int],
        range_num_spheres: tuple[int],
        range_num_cones: tuple[int],
        range_kube_size: tuple[float],
        range_sphere_radius: tuple[float],
        range_cone_radius: tuple[float],
        range_cone_height: tuple[float],
        range_light_height: tuple[float],
        range_num_lights: tuple[float],
        ):
    
    num_kubes = int(generate_random(*range_num_kubes))
    num_spheres_kubes = int(generate_random(*range_num_spheres))
    num_cones = int(generate_random(*range_num_cones))
    num_lights = int(generate_random(*range_num_lights))

    scene = {
        "id": id,
        "angle": generate_random(0, 2 * math.pi),
        "height": generate_random(*range_heigth),
        "fov": fov,
        "num_kubes": num_kubes,
        "num_spheres_kubes": num_spheres_kubes,
        "num_cones": num_cones,
        "num_lights": num_lights,
        "objects": {
            "kubes": [generate_kube(range_kube_size, plane) for _ in range(num_kubes)],
            "spheres": [generate_sphere(range_sphere_radius, plane) for _ in range(num_spheres_kubes)],
            "cones": [generate_cone(range_cone_radius, range_cone_height, plane) for _ in range(num_cones)],
            "lights": [generate_light(range_light_height, plane) for _ in range(num_lights)],
        }
    }

    return scene

if __name__ == "__main__":
    N = 300 # Number of scenes to generate
    OUTPUT_FILE = "gen/scenes.json"

    random.seed(123)

    scenes = []

    for n in range(N):
        scene = generate_scene_object(
            id=n,
            plane=100.0, 
            fov=70.0, 
            range_heigth=(70, 85),
            range_num_kubes=(0, 3),
            range_num_spheres=(0, 3),
            range_num_cones=(0, 3),
            range_kube_size=(10, 15),
            range_sphere_radius=(10, 30),
            range_cone_radius=(10, 15),
            range_cone_height=(10, 30),
            range_light_height=(80, 110),
            range_num_lights=(2, 5)
        )
        scenes.append(scene)
    
    with open(OUTPUT_FILE, "w") as f:
        json.dump(scenes, f)
    
    print("Generated", N, "items")
