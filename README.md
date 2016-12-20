This is a fork of [cpython](https://github.com/python/cpython), changed so as to add some(not yet all) features of [NonDex](https://github.com/TestingResearchIllinois/NonDex). 

## Setting up
After having cloned the repo, two steps should be sufficient:
```
./configure
make
```
The final `make` builds the source in the project directory itself. The executale is now accessible at `./python`.

## Running
To initiliaze seed for NonDex, set the environment variable `NONDEXSEED` to the required seed. Example:
```
export $NONDEXSEED="123"
```
The default seed is `1`, which is used when `NONDEXSEED` is not initialized or is not a valid numerical string.

## To-do
The current implemetation supports only `ONE` mode. Will include `FULL` mode soon.
Refer [here](http://mir.cs.illinois.edu/gyori/pubs/icst15nondex.pdf) for more details.
