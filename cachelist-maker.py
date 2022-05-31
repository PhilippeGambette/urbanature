import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths: list[str] = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            # support windows path
            filepath = filepath.replace('\\', '/')
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("./")

ext_exceptions = [".py", ".scss", ".map", "/_", "cachelist.js"]
dir_exceptions = [".git"]

with open('cachelist.js', 'w') as f:
    # write as a JS array of strings
    f.write('export const PRECACHE_URLS = [\n')
    for filepath in full_file_paths:
        is_writable = True
        for ext in ext_exceptions:
            if filepath.endswith(ext):
                is_writable = False
                break
        for dir in dir_exceptions:
            if filepath.startswith(f'./{dir}'):
                is_writable = False
                break
        if is_writable:
            f.write(f'    "{filepath}",\n')
    f.write(']')
