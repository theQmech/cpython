This is a fork of [cpython](https://github.com/python/cpython), changed so as to add some(not yet all) features of [NonDex](https://github.com/TestingResearchIllinois/NonDex). 

## Setting up
After having cloned the repo, two steps should be sufficient:
	./configure
	make
The final `make` builds the source in the project directory itself. The executale is now accessible via `./python`.

## Testing
Right now, we support a simple test. Use `./python test.py` to run the test.

## To-do
Only mode currently implemented is ONE. FULL also needs to be supported.

