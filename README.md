GeoJSON Centroid Calculator
===============

Methods for Calculating GeoJSON object centroids.

Features
--------

- Allows users to calculate geoJSON centroids and output them to JSON file


Project Organization
--------

This project is organized in the following manner:

<details><summary>Root directory: Contains all code needed to run the GeoJSON Centroid Calculator.</summary>
    <ul>
    <li>centroidcalculator.py: File containing functions for calculation of centroids.</li>
    <li>run.py: Easy access edit point for quick use</li>
    <li>zip3.json: Example json file of 3 digit zip codes in the US</li>
    <li>zip3Centroid.json: Example output json file</li>
    </ul>
</details>


Prerequisites
-------------

This project uses an extra package to work properly:

* [json] - A lightweight data interchange inspired by java script

How to Use
----------

Make sure you have Python 3.6.x installed on your system. You can download it [here](https://www.python.org/downloads/).

### Linux

1. Clone this repo in your preferred directory:
    ```sh
    $ git clone https://github.com/connor-makowski/geojson-centroid-calculator.git
    ```
2. Go to the root directory of the project using the `cd` command.
    ```sh
    $ cd geojson-centroid-calculator
    ```

### Getting Started

1. Put your GeoJSON data in the root project folder.
  - Your data should follow the GeoJSON pattern
    - An example can be found at `zip2.json`

2. Open up the run.py file with your favorite text editor.
3. Edit `infile=` (line 3) to exactly match your input data. For example:
    ```sh
    infile='zip3.json'
    ```

4. Edit `outfile=` (line 3) to exactly match your output data. For example:
    ```sh
    outfile='zip3Centroid.json'
    ```
5. Edit `propertiesId=` (line 3) to exactly match an identifier in your GeoJSON properties object. For example:
    ```sh
    propertiesId='ZIP3'
    ```

### Run Your Model

Use Python to execute the `run.py` file. This will import the centroidcalculator.py file and your data to process the results.
```sh
$ python run.py
```

Your output will be located in the same folder under the `outfile` you specified.

License
-------

Copyright (c) 2018 Connor Makowski
