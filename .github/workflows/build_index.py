import pathlib
import json


def main():
    # For any Scheme, we can generate a JSON file with the following format:
    json_dict = dict()

    for path in pathlib.Path(".").iterdir():
        json_dict[path.stem] = str(path)

    with open("index.json", "w") as f:
        json.dump(json_dict, f, indent=4)


if __name__ == "__main__":
    main()
