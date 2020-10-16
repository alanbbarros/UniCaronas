<h1 align="center">UniCaronas
</h1>
<h3 align="center">
🚘 We connect rides with UFG canoners efficiently 🚘
</h3>
<h4 align="center">
	🚧 Building 🚧
</h4>

## Content Table

 * [About the project](#-about-the-project)
 * [Functionalities](#-functionalities)
 * [Layout](#-layout)
 * [Technologies](#-technologies)
 * [Development](#-development)
  	* [Architecture](#architecture)
 	* [Prerequisites](#prerequisites)
 	* [Running the Backend](#running-the-backend)
 	* [Running the Frontend](#running-the-frontend)
 * [How to contribute](#-how-to-contribute)
 * [Authors](#-authors)


## 💻 About the project

This project is a mobile application that connects drivers and passengers
university students enrolled at the Federal University of Goiás. They can offer rides, view them or request them from a driver.

>Project developed during the Software Construction course at the Federal University of Goiás.

## 📱 Functionalities

- [x] Students enrolled at UFG have access to the mobile application, where they can:
	- [x] view rides offered by other students nearby
	- [x] request rides to a desired location
	- [x] offer rides to other students, given a place of departure and arrival
	- [x] set a specific value for your ride when they offer

## 🎨 Layout

The application layout is available on Figma [clicking here].

## 🛠 Technologies

The following tools are used in the construction of the project:

- [ ] React Native version xx
- [ ] Python version xx
- [ ] MongoDB version xx
- [ ] Heroku version xx
- [ ] Digital Ocean version xx
- [ ] Docker version xx

## 🚀 Development

### Architecture

- [ ] Architectural Diagram
<img src="https://raw.githubusercontent.com/CS2020-1-CavaloTroia/UniCaronas/master/arquitetura_UniCaronas.png" width="800">

- [ ] Technologies Diagram

<img src="https://raw.githubusercontent.com/CS2020-1-CavaloTroia/UniCaronas/master/tecnologias_UniCaronas.png" width="800">

### Prerequisites

Before starting, make sure you have on your machine:
- [ ] MongoDB database version xx or higher
- [ ] Node version xx or higher
- [ ] Yarn version xx or higher
- [ ] Python2 version xx or higher

Also, it’s good to have an editor to work with the code, like [VSCode](https://code.visualstudio.com/).

#### Installing React Native

- [ ] Follow the steps on [React Native](https://reactnative.dev/docs/0.61/getting-started)
- [ ] Select the type of installation **React Native CLI Quickstart** and your operating system

### Running the Backend

```bash
Clone this repository
$ git clone https://github.com/CS2020-1-CavaloTroia/UniCaronas

Access the project folder in your terminal / cmd
$ cd server/UniCaronas

Create a database
$ python manage.py migrate

Run the application
$ python manage.py runserver

The application will open at the port:8000 - acess http://localhost:8000
If you want to specify the port, use
$ python manage.py runserver <port>
```

#### Creating a database

>TODO passo a passo

Access keys:
- [ ] Homologation
>TODO

- [ ] Production
>TODO

### Running the Frontend

```bash
Clone this repository
$ git clone https://github.com/CS2020-1-CavaloTroia/UniCaronas

Access the project folder in your terminal/cmd
$ cd app/UniCaronas

Install the dependencies
$ yarn

Run the application in development mode
$ react-native run-is 
or
$ react-native run-android

```

## 💡 How to contribute

1. Fork the project.
2. Create a new branch with your changes: `git checkout -b my-feature`
3. Save your changes and create a commit message telling you what you did: `git commit -m "feature: My new feature"`
4. Submit your changes: `git push origin my-feature`

## 👨‍💻 Authors

Cavalo de Troia Group of 2020.1 Software Construction class at Federal University of Goiás
* Amanda Lobo Gomes
* Alan Brito Barros
* Fernando Severino Almeida
* Gustavo Ribeiro de Oliveira
* Michelly Silva Lima

## README versions

[Portuguese 🇧🇷](./README.md) | [English 🇺🇸](./README-en.md)
