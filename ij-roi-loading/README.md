# Loading objects from ImageJ ROI files
This script can be used to load objects from zipped ImageJ ROI files.  Currently, this is configured for files saved from the [ModularImageAnalysis (MIA)](https://github.com/mianalysis/mia) plugin, as these have additional position and ID information in .roi filenames.

## Requirements
- Python 3.8.10
- numpy==1.24.4
- pywin32==311
- roifile==2023.5.12
- arivis.vision4d (installed via Arivis software)

## Installation
- Download and install Python from [here](https://www.python.org/downloads/release/python-3810/)
- In terminal, create a new Python virtual environment
	`Python -m venv arivis`
- Activate python environment
	`[path to environment]/Scripts/activate`
- Install requirements
	`python -m pip install -r [path to [requirements.txt](./requirements.txt) file]`
