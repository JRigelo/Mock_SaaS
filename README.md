README
======

------------------------------------------------------------------------------

Contents
--------

A. Overview

B. Installation

  1. Software Dependencies

C. Documentation

  1. Running the Unit Tests
  2. Running the Application

--------------------------------------------------------------------------
A. Overview
------------

Prorated refund forecast model for the Mock SaaS project.
This Application provides basic support for forecasting prorated refunds
in order to provide a company a better understanding of the cash reserves
needed to be kept, daily or monthly.

--------------------------------------------------------------------------
B. Installation
---------------
To install dependencies, from root directory run

```
  pip install -r requirements.txt
```

### 1. Software Dependencies ###

- [python 2.7](https://www.python.org/)
- [pytest](http://doc.pytest.org/en/latest/)
- [yaml](http://yaml.org/)
- [Numpy](http://www.numpy.org/)
- [pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](https://seaborn.github.io/)

See the updated list of dependencies in the `requirements.txt` file.

--------------------------------------------------------------------------
C. Documentation
----------------

### 1. Running the Unit Tests ###

From the root directory run
```
make test        
```

### 2. Running the Application ##  

cd SaaSModel/
```       
ipython forecast.py ../input/model_input.yml ../output/mode_output.txt
```   

The repository has the following folder structure:  

```
Mock_SaaS   
  ├── Makefile    
  ├── README.md
  ├── requirements.txt    
  ├── SaaSModel    
  │     ├── __init__.py  
  |     ├── client.py  
  |     ├── finances.py    
  │     ├── forecast.py  
  ├── data  
  │     ├── membership.csv  
  ├── input
  │     ├── model_input.yml  
  ├── output
  └── test
        ├── __init__.py  
        ├── test_client.py  
        └── test_finances.py  
```
