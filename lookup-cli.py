import sys
import yaml

def print_manual():
    print("Usage: lookup-cli <name> <field_to_output>")
    sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print_manual()

    search_name = sys.argv[1]
    field_to_output = sys.argv[2]

    yaml_file_path = "data.yaml"

    try:
        with open(yaml_file_path, "r") as file:
            data = yaml.safe_load(file)

        # Find entry by search_name
        entry = None
        for item in data:
            if item["name"] == search_name:
                entry = item
                break
        if not entry:
            print("Name not found")
            sys.exit(1)

        # Retrieve output field
        value = entry.get(field_to_output)
        if value is None:
            print("Field not found")
            sys.exit(1)

        print(value)
    except FileNotFoundError:
        print("YAML file not found")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
