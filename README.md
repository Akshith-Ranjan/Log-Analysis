# Log-Analysis

This is the third project for the Udacity Full Stack Nanodegree. An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like

### Requirements:
- [Python3](https://www.python.org/downloads/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)

### Setup
  1. Install VirtualBox and Vagrant
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/sagarchoudhary96/Log-Analysis)
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  ```
    $ vagrant ssh
  ```
  3. Setting up the database:

  ```
    psql -d news -f newsdata.sql
  ```
  
### To Run
  ```
    $ loganalysis.py
  ```
