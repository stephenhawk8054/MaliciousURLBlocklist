def write_text(data, file_path):
    with open(file_path, 'w', encoding='utf-8', errors='surrogateescape') as fw:
        if isinstance(data, str):
            fw.write(data.strip())
        else:
            for item in data:
                fw.write(f'{item}\n')