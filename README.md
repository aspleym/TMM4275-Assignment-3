# TMM4275-Assignment-3

[![](https://img.shields.io/badge/HTML5-a?style=flat&logo=html5&label=Code&color=E34F26&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![](https://img.shields.io/badge/JavaScript-a?style=flat&logo=javascript&label=Code&color=F7DF1E&logoColor=ffffff)](https://www.javascript.com/)
[![](https://img.shields.io/badge/Python-a?style=flat&logo=python&label=Code&color=3776AB&logoColor=ffffff)](https://www.python.org/)
[![](https://img.shields.io/badge/CSS3-a?style=flat&logo=css3&label=Code&color=1572B6&logoColor=ffffff)](https://developer.mozilla.org/en-US/docs/Archive/CSS3)  
[![](https://img.shields.io/badge/VSCode-a?style=flat&logo=visual-studio-code&label=Editor&color=007ACC)](https://code.visualstudio.com/)
[![](https://img.shields.io/badge/NX-a?style=flat&logo=siemens&label=CAD&color=009999&logoColor=ffffff)](https://www.plm.automation.siemens.com/global/en/products/nx/)
[![](https://img.shields.io/badge/NXOpen-a?style=flat&label=Library&color=009999&logoColor=ffffff)](https://docs.plm.automation.siemens.com/data_services/resources/nx/11/nx_api/custom/en_US/nxopen_python_ref/index.html)  
![](https://img.shields.io/maintenance/no/2021)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Task](#task)
- [Sketch and diagrams](#sketch-and-diagrams)
- [Built With](#built-with)
  - [Libraries](#libraries)
  - [Face Detection Algorithm](#face-detection-algorithm)
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

Weldability check.

A welding robot has to weld walls to the base plane. Walls can be seen as a maze. The target is to find
and show all the volumes where the welding gun can fit.

From what we could understand from our class lectures, we misunderstood our previous task (CAD-based (robot trajectory) potential weld lines generation.).
We did not implement a system that used _.prt_-files and [_NXOpen - Python_](https://docs.plm.automation.siemens.com/data_services/resources/nx/11/nx_api/custom/en_US/nxopen_python_ref/index.html).
Instead we used a _.csv_-file to describe a maze structure, and created a _.dfa_-file that could be read in [Siemens NX](https://www.plm.automation.siemens.com/global/en/products/nx/).

Originally we wanted to build upon [our previous task](https://github.com/aspleym/TMM4275-Assignment-2) to extend the system and finish some of our roadmap goals, but decided to show that we can use _NXOpen_ with _.prt_-files since it is one of _TMM4275_'s competence requirements.
We therefor needed to remove some of our functionalities for this task, e.g. previews, some automation and Fuseki-server.

## Sketch and diagrams

### UI sketches:

|                                                    Homepage                                                    |                                                 Result page                                                  |
| :------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: |
| ![](https://github.com/aspleym/TMM4275-Assignment-3/blob/main/images/Weldability%20checker%20-%20Homepage.png) | ![](https://github.com/aspleym/TMM4275-Assignment-3/blob/main/images/Weldability%20checker%20-%20Result.png) |

### Architecture and Sequence diagrams:

|                                                      Architecture                                                      |                                                  Generate trajectory/maze                                                   |                                                Import/Export                                                 |
| :--------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: |
| ![](https://github.com/aspleym/TMM4275-Assignment-3/blob/main/images/Weldability%20Checker%20-%20UML-Architecture.png) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/UML-Notes-Sequence%20generate%20maze%20and%20path.png) | ![](https://github.com/aspleym/TMM4275-Assignment-2/blob/main/images/UML-Notes-Import_Export%20Sequence.png) |

## Built With

Everyone that contributed to the project used [Visual Studio Code](https://code.visualstudio.com/) to develop this software. The next section has a list of libraries and applications that have been used in this project. The names are linked to one of the developers home page for the library. Most of the libraries are included in the latest version of Python.

### Libraries

- [NXOpen - Python](https://docs.plm.automation.siemens.com/data_services/resources/nx/11/nx_api/custom/en_US/nxopen_python_ref/index.html)
- [http.server](https://docs.python.org/3/library/http.server.html)
- [socketserver](https://docs.python.org/3/library/socketserver.html)
- [Requests](https://requests.readthedocs.io/en/master/)
- [os](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [inspect](https://docs.python.org/3/library/inspect.html)
- [smtplib](https://docs.python.org/3/library/smtplib.html)

### Weld check Algorithm

TODO: Write a explenation on how it works, MAGNUUUUUUS

To find potetial weld edges we have decided to check the following criterias:

- Is it enough free space above the line to fit the robot?
- Is it enough free space next to the line to fit the robot?
- Is the line in Z = 0 and is it an edge connecting a wall and the base plate?

#### The Algorithm

The first body is assumed to be the base plate and is stored to be compared later. The faces and edges from the remaining bodies are stored in lists. Only edges on z = 0 are kept, and duplicates removed. It then sorts each face in three categories depending on which axis its parallel with. I.e., a face parallel with the x-axis is an x face. The faces are also sorted on its depth value. I.e., x faces are sorted in ascending y order.
The algorithm then loops through every potential edge. It tests both sides of the edge which in a local coordinate system is the first and second quadrant. For each quadrant it makes a 2d face of the robot, and then loops through every face orthogonal to the edge, in ascending order with respect to the depth value. For each face, it performs two main checks. Is the face before, equal to, or between the limits of the edge, and is the face intersecting the robots face?
If the first is true and it intersects the robots face, the algorithm knows a body is beginning and it needs to remember it. If another face appears before the limits of the edge, we know that this face closes of the first face and makes a body that is not intersecting with the edge.
If a face appears between the limits of the edge, and intersects with the face of the robot, we know that we can’t weld this line.
If two faces are exactly equal to the limits of the edge, and intersecting the face of the robot, we know that the robot must be inside the body that owns the edge. It can’t weld this side of the edge, and the algorithm moves on to check the quadrant on the other side of the edge.
If a line passes the tests, it gets welded with a green line in NX. Otherwise, the line is colored red. If the edge is owned by the
The test is performed on every y face for each x edges, and vice versa.

Limitations:

- The baseplate must go from Z = 0 to negative Z values
- The first sketch must contain the baseplate, and can't contain the rest of the model
- The rest of the model must be in it's own sketch and have positive Z values
- Only lines on Z = 0 can be a potential weld line
- Every wall must be orthogonal to one of the main axies x, y, z
-

## Getting Started

### Prerequisites

To run this project you would need to install [Python 3.9](https://www.python.org/) to run the website. To open a _.prt_-file and execute the _Face Detection Algorithm_, you would need [Siemens NX](https://www.plm.automation.siemens.com/global/en/products/nx/).

### Download project

This section will guide you to clone this git repository. Type the following lines in the terminal (for **_unix_** users), or Command Prompt (for **_windows_** users):

```sh
cd /to-your-desired-directory
git clone https://github.com/aspleym/TMM4275-Assignment-3.git
cd TMM4275-Assignment-3
```

You are now inside the project folder.

Type `ls` in the terminal, or `dir` in Command Prompt to see the root folder structure.

### Run the system

In this section you will be guided step by step on how to run the system on your computer.

#### Web server

- To run the Python server, start by opening a command-line interpreter like CMD (Command Prompt) or Termnial.
- Navigate to the project directory by using commands like `cd`.
- When inside project folder, type the following to check Python version:

```sh
python --version
```

- You should verify that you are using **Python 3**.
- To execute the web server, type the following and press enter:

```sh
python httpserver.py
```

- The web server should be available at: `127.0.0.1:8080` in a web browser.

## Usage

TODO: Write how to use, from the sender, and for the designer. Run on NX, automatic email etc.

**Customer:**  
The customer is able to tell the designer their email address and welding gun's dimensions. The welding gun will be intepreted as a block to make the weldability check simpler. By pressing the button _Choose file_, the customer will open a window and can direct the system to upload a _.prt_-file. When the _order_ is successful, an confirmation email will be sent to the customer and a notification email will be sent to the designer.

**Designer:**  
When the designer recieves a notification, they are able to find a folder with the order name inside the project directory's _Product_ folder. Inside the folder named after the uploaded _.prt_-file, there should be three files with the same name but different filename extension: _.prt_, _.ini_ and _.py_.

The _.ini_-file contains information about the order in this format:

```ini
NAME: Name of part file.
EMAIL: Email to the customer.
LENGTH: Length of welding robot.
WIDTH: Width of welding robot.
HEIGHT: Height of welding robot.
```

It is used by the system to configure the weldability checker that is generated (_.py_-file) in the same folder. The generated _.py_-file is pointing to the _Face Detector Algorithm_ and _.prt_-file, and can be executed in Siemens NX.

The designer can now open Siemens NX, then open the function _Edit Journal_, and direct to the customer's generated _.py_-file. After the algorithm is executed, there should be colored lines for where the robot is able to weld. A green line indicates the welding line to be reachable for the robot, and a red line indicated that it is not reachable.

### Limitations for the _.prt_-file

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
