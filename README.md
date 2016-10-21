# Mock_SaaS

## Overview

Prorated refund forecast model for the Mock SaaS project.
This Application provides basic support for forecasting prorated refunds
in order to provide a company a better understanding of the cash reserves
needed to be kept, daily or montly.

## Application Dependencies

- [python 2.7](https://www.python.org/)
- [pytest](http://doc.pytest.org/en/latest/)
- [yaml](http://yaml.org/)
- [Numpy](http://www.numpy.org/)
- [pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](https://seaborn.github.io/)


## Running the Unit Tests:
  from the root directory  
```
      make test        
```

## Running the Application:  


  cd code/
  ```       
  ipython forecast.py ../input/model_input.yml ../output/mode_output.txt
  ```   

The repository has the following folder structure:  

```

Mock_SaaS   
  ├── Makefile    
  ├── README.md  
  ├── code    
  │     ├── __init__.py  
  |     ├── client.py  
  |     ├── finances.py    
  │     ├── forecast.py  
  ├── data  
  │     ├── membership.csv  
  ├── input
  │     ├── model_input.yml  
  └── test
        ├── __init__.py  
        ├── test_client.py  
        └── test_finances.py  
```
