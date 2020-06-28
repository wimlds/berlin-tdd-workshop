# :construction::rotating_light: **DO NOT READ IF YOU ARE NOT A WORKSHOP INSTRUCTOR OR MENTOR!!!** :rotating_light: :construction:

% title: One step closer to unit testing in data science

% authors: Ellen König, Marielle Dado, Tereza Iofciu

---

# -> Unit testing

- [Presentation](https://docs.google.com/presentation/d/1Lc1fhpQsXWQonHNtZ78rozE_nymrFaoZuuGyp7q007Q/edit#slide=id.p1): what is unit testing, why, how and so on

---

# -> Where to start?

- Fork and clone the workshop repo: `git clone https://github.com/wimlds/berlin-tdd-workshop`
- follow setup instructions in README

- start environment (README)

- run first test in terminal: `pytest`

- let's look at the function in [scripts/imputation.py](scripts/imputation.py) and at the test in [test/test_imputation.py](test/test_imputation.py)

---

# -> Missing Values - Exercise 1

- start Jupyter Lab (terminal: `jupyter lab`)
- open the [EDA](EDA.ipynb) notebook
- the data has missing pricing values
- let's add different functions for imputing the data and more tests.
- running, in env run `pytest`
- change the imputation method and adapt test (example method is with mean)
  - some should do impute w max
  - some with min
  - think of test edge cases: calling this function on a column full of nans?
  - how will we name all the tests and functions
- copy the methods we write into [scripts/imputation.py](scripts/imputation.py) and at add the tests in [test/test_imputation.py](test/test_imputation.py)

---

# -> Transformations - Exercise 2

- checking the data open the [EDA](EDA.ipynb) notebook
- method is in [scripts/transformation.py](scripts/transformation.py) and at add the tests in [test/test_transformation.py](test/test_transformation.py)
- first data transformation method, it works in notebook but has error..
- comment out the skip test, run test.. (test will fail)
  - fix method so that test passes
  - write a test that explicitly does a type check
  - add test with different input data.. all values the same
- fix method (should return pd.Series(new_series))

# -> EDA - Exercise 3 and Homework

- Open the [EDA](EDA.ipynb) notebook
- let's write the test for the aggregate in the third exercise
  - here we add new python script and new test file
  - discuss the chicken and egg problem of notebooks and scripts..
- discuss homework .. notify in which channel people should upload their solutions (ideally everybody has forked the repo and would push their solutions to their version of the workshop)

---

# -> Closing

- Ask participants what they learned
- Let's watch the pockets video https://www.youtube.com/watch?v=Vi2Vgym6lbw
- Call to action: No pull request/ notebooks goes away without a script and a test!
