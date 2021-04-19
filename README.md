# TMM4275-Assignment-3

[![](https://img.shields.io/badge/HTML5-a?style=flat&logo=html5&label=Code&color=E34F26&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![](https://img.shields.io/badge/JavaScript-a?style=flat&logo=javascript&label=Code&color=F7DF1E&logoColor=ffffff)](https://www.javascript.com/)
[![](https://img.shields.io/badge/Python-a?style=flat&logo=python&label=Code&color=3776AB&logoColor=ffffff)](https://www.python.org/)
[![](https://img.shields.io/badge/CSS3-a?style=flat&logo=css3&label=Code&color=1572B6&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Archive/CSS3)  
[![](https://img.shields.io/badge/VSCode-a?style=flat&logo=visual-studio-code&label=Editor&color=007ACC)](https://code.visualstudio.com/)
[![](https://img.shields.io/badge/NX-a?style=flat&logo=siemens&label=CAD&color=009999&logoColor=ffffff)](https://www.plm.automation.siemens.com/global/en/products/nx/)  
![](https://img.shields.io/maintenance/no/2021)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Task](#task)
- [Sketch and diagrams](#sketch-and-diagrams)
- [Built With](#built-with)
  - [Libraries](#libraries)
  - [Face detection Algorithm](#face-detection-algorithm)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Download project](#download-project)
  - [Run the system](#run-the-system)
- [Usage](#usage)
- [Examples](#examples)
- [Roadmap](#roadmap)
- [File Structure](#file-structure)
- [Contributors](#contributors)
- [License](#license)

## Task

TODO: Add an introduction to the final task, what we decided to change, why etc.

Weldability check.

A welding robot has to weld walls to the base plane. Walls can be seen as a maze. The target is to find 
and show all the volumes where the welding gun can fit.

## Sketch and diagrams

### UI sketches:

|                                                   Homepage                                                    |                                                 Result page                                                 |
| :-----------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------: |
| ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/Welding%20trajectory%20-%20Homepage.png) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/Welding%20trajectory%20-%20Result.png) |

### Architecture and Sequence diagrams:

|                                           Architecture                                           |                                                  Generate trajectory/maze                                                   |                                                Import/Export                                                 |
| :----------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: |
| ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/UML-Notes-Architecture.png) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/UML-Notes-Sequence%20generate%20maze%20and%20path.png) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/UML-Notes-Import_Export%20Sequence.png) |

## Built With

Everyone that contributed to the project used [Visual Studio Code](https://code.visualstudio.com/) to develop this software. The next section has a list of libraries and applications that have been used in this project. The names are linked to one of the developers home page for the library.

### Libraries

- [http.server](https://docs.python.org/3/library/http.server.html)
- [socketserver](https://docs.python.org/3/library/socketserver.html)
- [Requests](https://requests.readthedocs.io/en/master/)
- [os](https://docs.python.org/3/library/os.html)

### Face detection Algorithm
TODO: Write a explenation on how it works


## Getting Started

### Prerequisites

To run this project you would need to install [Python 3.9](https://www.python.org/) to run the website.

### Download project

This section will guide you to clone this git repository. Type the following lines in the terminal (for **_unix_** users):

```sh
cd /to-your-desired-directory
git clone https://github.com/aspleym/TMM4275-Assignment-3.git
cd TMM4275-Assignment-3
```

You are now inside the project folder.

Type `ls` in the terminal to see the root folder structure.

### Run the system

In this section you will be guided step by step on how to run the system on your computer.

#### Web server

- To run the Python server, start by opening a command-line interpreter like CMD or Termnial.
- Navigate to the project directory by using commands like `cd`.
- When inside project folder, type the following to execute check Python version:

```sh
python --version
```

- You should verify that you are using **Python 3**.
- To execute the web server, type the following and press enter:

```sh
python httpserver.py
```

- The web server should be available at: `127.0.0.1:8080` in the web browser.

## Usage

TODO: Write how to use, from the sender, and for the designer. Run on NX, automatic email etc.

### Create your own maze

TODO: Rules for how the .prt - file should be for the algorithm to work.

## Examples

You can try out a demo of this project [here!](https://wc.magnusolstad.no)

### Weldability check examples (Templates)

|                                        Low                                        |                                        Medium                                        |                                        High                                        |                                        Extreme                                        |
| :-------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/LowMaze.PNG) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/MediumMaze.PNG) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/HighMaze.PNG) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/ExtremeMaze.PNG) |

### Overview of the "extreme" maze template

![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/ExtremeMazeOverview.PNG)

## Roadmap

TODO: Last task, what we wished we could have done.

## File structure

This is an overview of the file structure for this repository and a short explanation for some of the files.

```
TMM4275-Assignment-2
│   .gitignore                          A file to tell Github to ignore files.
│   httpserver.py                       httpserver.py: Python script to execute a http server and request handler for the customer.
│   LICENSE                             Standard license file to tell it's class of license.
│   queries.txt                         A txt file with examples for some of the queries in SPARQL.
│   README.md                           This file.
│
├───DFA                                 Templates for generating DFA-files.
│   │   MazeAndTrajectoryTemplate.dfa
│   │   MazeTemplate.dfa
│   │   TrajectoryTemplate.dfa
│   │
│   └───products                        Where we store generated DFA-files.
│
├───Fuseki                              The folder for the Fuseki sever.
│
├───images                              Images for the README.
│
├───Maze                                Maze description files. Templates as both csv and xlsx (Excel) files.
│   │   Template.csv
│   │   Template.xlsx
│   │
│   └───Uploaded
│           maze0.csv                   Predefined maze with low complexity
│           maze1.csv                   Predefined maze with medium complexity
│           maze2.csv                   Predefined maze with high complexity
│           maze3.csv                   Predefined maze with extreme complexity
│
├───OWL
│       shapes.owl                      The OWL model.
│
├───Python
│   │   fusekiposter.py                 The Python file that contains functions to post and get trajectories from the Fuseki server.
│   │   generateDFA.py                  Functions to generate DFA files of trajectory and maze.
│   │   Maze.py                         Python file to create a Maze model. Contains pathfinding algorithm and helper functions
│   │   MazeReader.py                   Python file to read or write csv-files from server and return it as an array
│
└───Wall-E
    │   index.html                      This is the html file for our Homepage.
    │   main.css                        Styling for index.html.
    │   order.css                       Styling for the result page.
    │   order.html                      The result page giving a download link for the DFA-file.
    │
    └───js
            index.js                    Multiple scripts used to handle events on the website.
            OrbitControls.js            Camera library for Three.js.
            three.js                    Three.js Library.
            three.min.js
            three.module.js
```

## Contributors

[<img src="https://github.com/Magwest1.png?size=50" alt="" data-canonical-src="" width="50" height="50" />](https://github.com/Magwest1)  
Magnus Ølstad

[<img src="https://github.com/aspleym.png?size=50" alt="" data-canonical-src="" width="50" height="50" />](https://github.com/aspleym)  
Adrian Pleym

## LICENSE

Distributed under the [MIT](https://opensource.org/licenses/MIT) License.
