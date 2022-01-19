import os
dirs = [os.path.join("data","raw"),
        os.path.join("data","process"),
        "notebooks",
        "saved_models",
        "src"
        ]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir,".gitkeep")) as f :
        pass

        ]