
# Machine Learning Engineer Nanodegree

## Supervised Learning

### Project: Classifying instagram photos using deep learning techniques

####  Install

This project requires Python 2.7.12 or above and the following Python libraries installed:

    NumPy
    Pandas
    matplotlib
    scikit-learn

We recommend to install Anaconda, a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. Furthemore, you need to install the _IPython shell_ along with _Jupyter_. 


#### Results

All the results and models are described and summarized in _Report.pdf_.

#### Run

In a terminal or command window, navigate to the top-level project directory capstone_project/ (that contains this README) and run the following command:


```python
jupyter notebook
```

This will open the Jupyter Notebook software and project file in your browser.
You'll notice that this project contains two folders:

- Data: It contains all the data used to build the models and also a python script that was used to download this data.
- Source: It contains all the code resposible for building and evaluating the models. In here, you'll find the below notebooks:
	- **KNN.ipynb**: It builds the benchmark model
	- **DeepLearning.ipynb**: It builds the first deep learning architecture.
	- **DeepLearning-CNN.ipynb**: It builds the second deep learning architecture.
	- **Report.ipynb**: Notebook that creates the Report.pdf file.

#### Data

All the data used here was collected from the _instagram_ social network and using the script in the _Data/crawler.py_. All the instructions that are needed to run this script are documented in the _Data/readme.md_ file. 