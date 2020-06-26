% title: One step closer to unit testing in data science

% authors: Ellen König, Marielle Dado, Tereza Iofciu

---

# -> Unit testing

- Presentation: what is unit testing, why, how and so on

---

# -> Where to start?

- follow setup instructions in README

- start environment (README)

- start Jupyter Lab (-> jupyter lab)

---

# -> Dataset

- Let's look at some pockets data
- Clone the workshop repo: `git clone https://github.com/wimlds/berlin-tdd-workshop`
- Go to folder `cd berlin-tdd-workshop`
- Download .json file from : `git clone https://github.com/the-pudding/data.git`
- file needs to be opened from editor and saved.. to fix json encoding issue
- copy data/pockets/measurementRectangles.json file to workshop folder
- to take a look at the data open and run cells in the [DataProfiling](DataProfiling.ipynb) notebook
- we see that data is nicely balanced, each brand has 4 jeans, 2 for men and 2 for women and no missing data

---

# -> Missing Values

- the data doens't have any missing values so we are going to artificially create some
- follow instructions in the [DataProfiling](DataProfiling.ipynb) notebook
- let's write our first test for the data imputing function
- running tests: `make test` or in env run `pytest`
- change the imputation method and adapt test (example method is with mean)
  - some should do impute w max
  - some with min
  - some with and some with random value between min and max (advanced)
- the methods we write are in [data_preparation](data_preparation.py) script

---

# -> Back to the data - EDA - Exercise 1

- disclaimer, the purpose of this is not to do eda or be correct about or eda :D
- checking some data assumptions, open the [EDA](EDA.ipynb) notebook
- first data transformation method, it works in notebook but has error..
- comment out the skip test, run test.. (test will fail)
- fix method (should return pd.Series(new_series))

# -> EDA - Exercise 2

- Open the [EDA](EDA.ipynb) notebook
- let's write the test for the aggregate in the second exercise
- discuss homework .. if there is time start with the exercise

---

# -> Closing

- Let's watch the pockets video https://www.youtube.com/watch?v=Vi2Vgym6lbw
