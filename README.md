# TMM4275-Assignment-3

[![](https://img.shields.io/badge/HTML5-a?style=flat&logo=html5&label=Code&color=E34F26&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![](https://img.shields.io/badge/JavaScript-a?style=flat&logo=javascript&label=Code&color=F7DF1E&logoColor=ffffff)](https://www.javascript.com/)
[![](https://img.shields.io/badge/Python-a?style=flat&logo=python&label=Code&color=3776AB&logoColor=ffffff)](https://www.python.org/)
[![](https://img.shields.io/badge/CSS3-a?style=flat&logo=css3&label=Code&color=1572B6&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
[![](https://img.shields.io/badge/Code-Json-informational?style=flat&logo=json&logoColor=white&color=000000)](https://www.json.org/json-en.html)  
[![](https://img.shields.io/badge/VSCode-a?style=flat&logo=visual-studio-code&label=Editor&color=007ACC)](https://code.visualstudio.com/)
[![](https://img.shields.io/badge/Excel-a?style=flat&logo=microsoft-excel&label=Utility&color=217346&logoColor=ffffff)](https://www.microsoft.com/en-ww/microsoft-365/excel)
[![](https://img.shields.io/badge/Three.js-a?style=flat&logo=three.js&label=Library&color=000000&logoColor=ffffff)](https://threejs.org/)
[![](https://img.shields.io/badge/Fuseki-a?style=flat&logo=apache&label=Server&color=D22128&logoColor=ffffff)](https://jena.apache.org/documentation/fuseki2/index.html)  
![](https://img.shields.io/maintenance/no/2021)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Task](#task)
- [Sketch and diagrams](#sketch-and-diagrams)
- [Built With](#built-with)
  - [Libraries](#libraries)
  - [Trajectory Algorithm](#trajectory-algorithm)
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

CAD-based (robot trajectory) potential weld lines generation.

A welding robot has to weld walls to the base plane. Walls can be seen as a maze. The target is to find  
all the edges connecting walls to the base plane. Having a maze-like structure, develop a
KBE solution to generate potential welding lines.

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

- [Three.js](https://threejs.org/)
- [http.server](https://docs.python.org/3/library/http.server.html)
- [socketserver](https://docs.python.org/3/library/socketserver.html)
- [Requests](https://requests.readthedocs.io/en/master/)
- [os](https://docs.python.org/3/library/os.html)
- [json](https://docs.python.org/3/library/json.html)
- [pandas](https://pandas.pydata.org/)

### Trajectory Algorithm

<img align="right" src="https://camo.githubusercontent.com/7ea38bf594e2982a200d937c69bee021d603d810d9b9187230faa0f43ccf25ee/687474703a2f2f7265732e636c6f7564696e6172792e636f6d2f647172326d656a68632f696d6167652f75706c6f61642f76313530313336303734362f6266735f7373776d657a2e676966">
To solve the trajectory problem, we decided early on to use one of the well known pathfinding algorithms. They usualy have a known target from the beginning,
and finds a path to the target. For this problem, our target were every side of a wall. We decided to use a Breadth-first search algorithm, since it wasn't depending on
searching for a specific target. Since we already needed to check every position in the maze, we could easly use this algorithm to find the closest wall that needed to 
be welded. Further the algorithm kept continously weld lines around the maze until it had welded every edge of the wall. Some walls were not connected to the previous wall, therefor the algorithm would search for other walls that were reachable and not welded to the base plane.

## Getting Started

### Prerequisites

To run this project you would need to install [Python 3.9](https://www.python.org/) to run the website and [Java](https://www.java.com/en/) if you want to run the Fuseki server with Java.
There is also a need for a Python library to be installed, [Pandas](https://pandas.pydata.org/).

Pandas can easly be installed via pip for PyPi. Open Command prompt or a Terminal and type in the following:

```sh
pip install pandas
```

### Download project

This section will guide you to clone this git repository. Type the following lines in the terminal (for **_unix_** users):

```sh
cd /to-your-desired-directory
git clone https://github.com/aspleym/TMM4275-Assignment-2.git
cd TMM4275-Assignment-2
```

You are now inside the project folder.

Type `ls` in the terminal to see the root folder structure.

### Run the system

In this section you will be guided step by step on how to run the system on your computer.

#### Fuseki server

- Go to the directory of the project
- Enter the directory for the Fuseki server, `Fuseki`.
- Execute one of the fuseki-server files depending on your operating system:
  - fuseki-server `UNIX`
  - fuseki-server.bat `WINDOWS`
  - fuseki-server.jar `JAVA`

#### Adding OWL model

- To add the OWL model to the server, open a web browser and type in the following un the URL field: `127.0.0.1:3030`.
- Locate the dataset named /kbe: `http://127.0.0.1:3030/dataset.html`
- Select the tab _upload files_ and then hit the button _+ select files..._ to add the OWL-model to the Fuseki server.
  - The owl file should be: `project-directory/OWL/shapes.owl`
- Press the button _upload all_ and verify that the upload was successful.

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

The website _Wall-E_ is able to read imported csv-files made by a user, or use premade templates of different complexities, to load a Maze.

If the user imports a csv-file, the file will be stored on the server. The premade templates are already stored on the server.

A preview of the loaded maze will be presented in the preview box to the right using *three.js* library.

When the user clicks _Generate Trajectory_ the page will generate a welding trajectory for the given maze. The trajectory will be stored on the fuseki server.

A DFA generator will read the trajectory from the fuseki server and make a DFA-file displaying the trajectory and the maze.

The user will be redirected to _order.html_ where it is possible to download the generated DFA-file

### Create your own maze

- Open the excel document located at `Maze/Template.xlsx`.
- 1 represents open areas, while -1 represent walls.
- These numbers can be changed to make your own maze.
- If you highlight a cell, and drag the small square in the bottom right corner, the number in the cell will be copied to the area you drag it over. This can be used to quickly create or remove walls.
- NOTE: cell (0,0) must be 1 as the pathfinding algorithm starts in this corner. If you block this square, the algorithm will not find a trajectory.
- When you are done, select _save as_ and choose _.csv_ as file type. Quickly open the file in notepad and make sure the numbers are seperated with semicolons `;`.
- This file can now be imported to Wall-E.

## Examples

You can try out a demo of this project [here!](https://walle.magnusolstad.no)

### Maze and trajectory examples (Templates)

|                                        Low                                        |                                        Medium                                        |                                        High                                        |                                        Extreme                                        |
| :-------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/LowMaze.PNG) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/MediumMaze.PNG) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/HighMaze.PNG) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/ExtremeMaze.PNG) |

### Overview of the "extreme" maze template

![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/ExtremeMazeOverview.PNG)

## Roadmap

We were not able to complete all of our goals for this project because of the limited time and other school tasks.  
There were some parts of the project we wished to improve upon. We will list them down here for other people to have an idea of what to do next. We aim to implement some of these features in assignment 3.

#### Website:

- Users should be able to input the dimensions for the "maze".
- Reduce possible bugs with wrong inputs. Import file etc.
- A preview of the trajectory using three.js.
- Option to export random generated mazes.

#### Python:

- Generate random mazes with different complexities.

#### Fuseki:

- Store maze in Fuseki. As of now we read a uploaded csv-file.

#### NX:

- Change color on the trajectory depending on whether or not the welding robot is welding, or just moving. This information can already be returned from the pathfinding algorithm.
- Improve DFA file to optimize construction time in NX.

We have no further plans for this school project. Until there are changes to our roadmap, this project will have no maintenance of the code as of 26. Mars 2021.

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
