import os, yaml, subprocess

with open("build.yaml") as f:
    manifest = yaml.safe_load(f)

os.makedirs("dist", exist_ok=True)

for g in manifest["graphs"]:
    name = g["name"]
    path = g["path"]

    print(f"Compiling Ab Initio graph: {name}")

    # MOCK compile (replace with air compile in real env)
    out = f"{name}"
    os.makedirs(out, exist_ok=True)
    subprocess.run(["cp", "-r", path, out], check=True)

    print("Generating ETL component")
    subprocess.run(
        ["bash", "build/generate_component.sh", name, out],
        check=True
    )

print("ETL component build complete")
