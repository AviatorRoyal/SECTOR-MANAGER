import os

def decimal_to_dms(degree, is_lat=True):
    direction = 'N' if is_lat else 'E'
    deg = int(degree)
    minutes_float = abs((degree - deg) * 60)
    minutes = int(minutes_float)
    seconds = round((minutes_float - minutes) * 60, 3)
    return f"{direction}{abs(deg):02d}.{minutes:02d}.{seconds:06.3f}"

def parse_line(line):
    parts = line.strip().split()
    if len(parts) != 3:
        return None
    name, lat, lon = parts[0], float(parts[1]), float(parts[2])
    return name, lat, lon

def convert_entry(name, lat, lon):
    lat_dms = decimal_to_dms(lat, is_lat=True)
    lon_dms = decimal_to_dms(lon, is_lat=False)
    return f"{name:<8}{lat_dms}  {lon_dms}"

def load_existing(file_path):
    entries = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    entries[parts[0]] = line.strip()
    return entries

def main(input_file, output_file):
    existing_entries = load_existing(output_file)
    new_entries = {}

    with open(input_file, 'r') as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                name, lat, lon = parsed
                if name not in existing_entries and name not in new_entries:
                    formatted = convert_entry(name, lat, lon)
                    new_entries[name] = formatted

    combined = {**existing_entries, **new_entries}
    sorted_entries = dict(sorted(combined.items()))

    with open(output_file, 'w') as f:
        for line in sorted_entries.values():
            f.write(line + '\n')

    print(f"Added {len(new_entries)} new entries. Total entries: {len(sorted_entries)}")

if __name__ == "__main__":
    main("input.txt", "output.txt")
