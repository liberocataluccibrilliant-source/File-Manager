#  Python File Manager CLI

A simple but versatile command-line file manager written in Python.  
This project allows users to create, read, write, rename, verify, clean, open, and delete files directly from the terminal with support for multiple file formats.

---

## Features

- Create files with automatic initialization for:
  - `.txt`
  - `.json`
  - `.csv`
  - `.md`
  - `.ini`

- Read file contents directly from the terminal
- Write content into supported files
- Delete existing files
- Empty/Clean file contents
- Rename files
- Verify:
  - if a file exists
  - file extension
- Open files from the program
- Display all files in the current directory
- Simple interactive CLI menu

---

## Supported File Types

| Extension | Support |
|----------|----------|
| `.txt` | Full |
| `.json` | Full |
| `.csv` | Full |
| `.md` | Full |
| `.ini` | Partial |

---

## Technologies Used

- Python 3
- `os`
- `pathlib`
- `json`
- `csv`
- `configparser`


---

## Example Commands

```text
/create_file
/write_file
/read_file
/delete_file
/show_files
/rename_file
/quit
```

---

## Notes

- Some functions such as `os.startfile()` are Windows-specific.
- The project was made for learning purposes and to practice:
  - file handling
  - CLI applications
  - Python standard libraries
  - error handling

---

## Future Improvements

- Better exception handling
- Cross-platform support
- Improved UI/UX
- Logging system
- Search functionality
- File copy/move support
- Colored terminal interface

---

## License

This project is open-source and available under the MIT License.
