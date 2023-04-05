import json 

SCENE_JSON = "/home/manus/Documents/Development/go/github.com/ubombar/monte-carlo-denoising/gen/scenes.json"

if __name__ == "__main__":
    with open(SCENE_JSON, "r") as f:
        scene_list = json.load(f)
    
    for scene in scene_list:
        print(scene)
        break