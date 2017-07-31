# Python Project Template

This project provides a best-practice template for any generic Python project. It integrates several different tools for documentation, code checking and unittests.

## How to
1. Clone the python project template and replace `project_template` with your project name
```
cd your_root_projects_directories
git clone https://github.com/DahuaCoder/PythonProjectTemplate.git projectname
cd projectname
```

2. Replace directory and file names with your project name

3. Verify personal text in readme and setup files

4. Reinit git repository
```
rm -rf .git && git init
```

5. (Optional) install virtualenv
```
mkvirtualenv --no-site-packages -p /usr/bin/python2.7 env_projectname
```

6. (Optional) install packages
```
pip install -r requirements.txt
```

## Documentation
We use Sphinx to generate documentation. All files related to documentation are located in the docs directory.
Tutorial: http://www.sphinx-doc.org/en/stable/tutorial.html

### Install Sphinx
```
$ pip install Sphinx
```

### Setting up the documentation sources
```
$ sphinx-quickstart
```