import pathlib
import json
import sys
import hashlib


def hashfile(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_rawlink(repo, scheme_name, length, version, file) -> str:
    return f"https://raw.githubusercontent.com/{repo}/main/{scheme_name}/{length}/{version}/{file}"


def parse_version(
    version_path, repo_url, scheme_name, length, version
) -> dict[str:str]:
    version_dict = dict()

    # Get the raw link for the primer.bed file
    for file in version_path.iterdir():
        if file.name == "primer.bed":
            version_dict["primer.bed.url"] = get_rawlink(
                repo_url, scheme_name, length, version, file.name
            )
            version_dict["primer.bed.md5"] = hashfile(file)

    return version_dict


def parse_length(length_path, repo_url, scheme_name, length) -> dict[str:str]:
    length_dict = dict()

    # Get all the versions
    for version in length_path.iterdir():
        # Only add directories
        if not version.is_dir():
            continue

        # Parse the version
        version_dict = parse_version(
            version_path=version,
            repo_url=repo_url,
            scheme_name=scheme_name,
            length=length,
            version=version,
        )

        # Add the version to the length dict
        length_dict[version] = version_dict

    return length_dict


def parse_scheme(scheme_path, repo_url, scheme_name) -> dict[str:str]:
    scheme_dict = dict()

    # Get all the lengths
    for length in scheme_path.iterdir():
        # Only add directories
        if not length.is_dir():
            continue

        # Parse the length
        length_dict = parse_length(
            length_path=length,
            repo_url=repo_url,
            scheme_name=scheme_name,
            length=length,
        )

        # Add the length to the scheme dict
        scheme_dict[length] = length_dict

    return scheme_dict


def main():
    # For any Scheme, we can generate a JSON file with the following format:
    json_dict = dict()

    # REPO url
    # https://github.com/quiicl-lab/primerschemes
    server_url = sys.argv[1]
    repo_url = sys.argv[2]

    for path in pathlib.Path(".").iterdir():
        # Only add directories
        if not path.is_dir():
            continue

        # Get the Scheme name
        scheme_name = path.name
        json_dict[scheme_name] = parse_scheme(path, repo_url, scheme_name)

    with open("index.json", "w") as f:
        json.dump(json_dict, f, indent=4)


if __name__ == "__main__":
    main()
