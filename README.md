# PE Track: Week 2 - Emilie Zhang - Portfolio Site

## Introduction

Previously, I created a team portfolio with TEAM PYTHONIC from Pod 22.SUM.21 of the Production Engineering Track at the MLH Fellowship.

Week 2 and onwards, this repository was forked from the original repo for customization of a personal portfolio and using production engineering best practices to host, scale, CI/CD and troubleshoot the application. 

In addition, this portfolio is hosted on a CentOS Stream 8 Oracle VPS instance. Accessible at: https://emiliezhang.duckdns.org/

#### Tech stack
__Backend:__ Flask Python, Jinja, json, Google Maps API, MySQL database, POST/GET/DELETE endpoints

__Frontend:__ HTML5/CSS, Javascript, Bootstrap framework

__Monitoring Tools:__ Prometheus, Grafana, cAdvisor

__CI/CD:__ unittest python library, redeploy-site.sh bash script, Github Actions workflows for Automated Continuous testing and deployment

__Docker Containers:__ Reverse Proxy for SSL termination, Nginx for traffic redirection and rate limiting on POST endpoint per IP

__Extra - Github Actions - Discord status notification:__ Github workflows are connect to personal Discord webhook. Sends a real-time message notifying developper of application build success status.

## Badges

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MLH-Fellowship/project-team-pythonic)
![GitHub repo size](https://img.shields.io/github/repo-size/MLH-Fellowship/project-team-pythonic)
![GitHub](https://img.shields.io/github/license/MLH-Fellowship/project-team-pythonic)

## Description

This is a reusable portfolio template which can be easily adapted to any number of team members. It is also mobile-friendly, which is an important feature considering that 50%+ of traffic on the web comes from mobile devices.

This personal portfolio website consists of two main components:

###### Landing page

- Animated heading text to display team name
- Medium subheading, animated text to display team info
- Profile picture of each member which leads to their respective profile pages

###### Profile page

Cards with relevant profile sections, including:
- About me
- Experience
- Projects
- Countries I've visited: Interactive Google Map with markers of locations each member has visited
- Hobbies: Hover effect tooltip boxes which display more information

###### Additional features

- Landing page with pop-up CSS animations when user hovers over main text
- Fully responsive website that adjusts according to screen size and works on mobile screens
- Animated menu bar for switching profiles or pages

## Visuals

##### Landing page

![image](https://user-images.githubusercontent.com/68432655/173205711-f83f84a7-7b5c-494d-ac07-bc4b6eebd045.png)

## File Structure

```
main
│   README.md                               # You're reading this now!
|   LICENSE.md                              # Details of this project's MIT license
│   .gitignore                              # Files to be ignored by git
|   .python-version                         # Python version used to build the project
|   example.env                             # An example of what your .env should look like
|   requirements.txt                        # Requirements for Python dependencies to install using pip
|   data.json                               # Database containing info to be loaded into the app
│
└───app
    │   __init__.py                         # The Python init file that runs upon executing "flask run"
    │
    └───static
    |   └───fonts
    |   |   |   flux-regular.otf            # The same font style used by Python (free to use)
    |   |
    |   └───img
    |   |   |   (all images for website)    # Various images used in the project
    |   |
    |   └───scripts
    |   |   |   index.js                    # Script containing animation triggers for the landing page
    |   |   |   maps.js                     # Script that loads the Google Maps API into the DOM
    |   |   |   profile.js                  # Script containing animation trigger for the hamburger menu
    |   |
    |   └───styles
    |   |   |   index.css                   # Styles and animations for the landing page
    |   |   |   maps.css                    # Styles for the Google Map on profile page
    |   |   |   profile.css                 # Styles for static components on profile page
    |
    └───templates
        |   index.html                      # Template for the landing page
        |   profile.html                    # Template for the profile page
        
```

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy of the file, then replace the values if required)

*Note: Add your own Google Maps API key in the .env file in order to use the map functionality*

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will work on your local machine while you have it running inside of your terminal. The portfolio is also hosted in a DigitalOcean droplet and deployed with Docker containers, thus accessible at https://emilieportfolio.duckdns.org/* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Tasks
Each of the following tasks are suggestions and/or programming best practices.

### GitHub Tasks
- [x] Create Issues for each task below
- [x] Work on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [x] Add a photo of yourself to the website
- [x] Add an "About youself" section to the website.
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions.
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies.
- [x] Add a menu bar that dynamically displays other pages in the app

## Acknowledgements
- [Google Maps API](https://developers.google.com/maps)
- [Bootstrap](https://getbootstrap.com)
- [FontsGeek](https://fontsgeek.com)
- [jonasal/nginx-certbot](https://hub.docker.com/r/jonasal/nginx-certbot) for generating Nginx certifications from LetsEncrypt

## Authors
* Emilie Zhang ([EmilieYZhang](https://github.com/EmilieYZhang))
* Forked repository from TEAM Pythonic's team portfolio
