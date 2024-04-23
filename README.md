# PDF Merger Script
### Introduction

This Python script merges multiple PDF files into a single PDF document. It employs the PyPDF2 library for PDF manipulation and the natsort library for natural sorting of file names. This README provides comprehensive information on using the script effectively.
### Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.x 
- PyPDF2 library (`pip install PyPDF2`) 
- natsort library (`pip install natsort`)
### Usage
#### Running the Script

To merge PDF files, execute the script in a Python environment. By default, it merges PDFs in the current directory. Optionally, you can specify a directory path containing the PDFs to merge.

```bash
python merge_pdfs.py [directory_path]
```


#### Script Parameters 
- `directory_path`: (optional) Path to the directory containing PDF files to merge. If not specified, the script merges PDFs in the current directory.
### Output

The merged PDF file is saved in the same directory as the script with the following naming convention:

```csharp
[Directory Name]_Merged.pdf
```


### Functionality 
1. **PDF Collection** : The script traverses the specified directory (or current directory) to collect PDF files for merging. 
2. **Natural Sorting** : PDF files are sorted naturally, ensuring a predictable order for merging. 
3. **Bookmark Generation** : Each merged PDF file is bookmarked with its filename (without the '.pdf' extension). 
4. **Merging** : The script merges the PDF files into a single PDF document while preserving bookmarks. 
5. **Output** : The merged PDF is saved with an appropriate filename in the same directory.
### Example

Suppose you have the following PDF files in a directory: 
- `document1.pdf` 
- `document2.pdf` 
- `document3.pdf`

Executing the script will merge these files into a single PDF named `Merged.pdf`.
### Note
- Ensure that the PDF files to be merged are not open or in use by any other application during script execution.
- Existing merged PDF files with the same name as the output filename will be overwritten without warning.
### License

This script is provided under the [MIT License]() .
### Contributors
- [Hamed/qerope]
### Issues

For any issues or suggestions, please open an [issue](https://github.com/qerope/PDF-Merger-Script/issues)  on GitHub.
### Acknowledgments

Special thanks to the authors and contributors of PyPDF2 and natsort libraries for their valuable contributions.
### Contact

For further inquiries, contact the owner of the repo.---
