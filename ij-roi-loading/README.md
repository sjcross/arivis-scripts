# Loading objects from ImageJ ROI files
This script can be used to load objects from zipped ImageJ ROI files.  Currently, this is configured for files saved from the [ModularImageAnalysis (MIA)](https://github.com/mianalysis/mia) plugin, as these have additional position and ID information in .roi filenames.

## Requirements
- Python 3.8.10
- numpy==1.24.4
- pywin32==311
- roifile==2023.5.12
- arivis.vision4d (installed via Arivis software)

## Installation
1. Download and install Python from [here](https://www.python.org/downloads/release/python-3810/)
2. In terminal, navigate to target folder into which environment will be created
3. Create a new Python virtual environment
	```console
	python -m venv arivis
	```
4. Activate python environment
	```console
	./arivis/Scripts/activate
 	```
5. Install requirements
   - Either use the following command to install requirements from requirements.txt file
		```console
		python -m pip install -r [path to requirements.txt file]
 		```
   - Or, use the following command to install the dependencies
   		```console
		python -m -pip install numpy==1.24.4 pywin32==311 roifile==2023.5.12
   		```
7. Open Arivis Vision4D/Pro and go to Extras > Preferences
8. Select "Scripting" from left side
9. Select "External Python Interpreter" and select Python.exe within new environment folder
10. Click "Install arivis package"
11. Click "Test Environment" to ensure everything is set up correctly

## Usage
1. Within Arivis Vision4D/Pro, go to Extras > Script editor
2. Open [ij-roi-loading.py](./ij-roi-loading.py)
3. Change "zip_path" variable to location of zipped ROI file, then click "Run script" button (green triangle)
