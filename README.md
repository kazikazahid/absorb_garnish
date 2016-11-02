# Problem

Setting up C++ for unit testing is time consuming from the command line,
especially for small projects, or experimental programs.

# Goal

Provides C++ project set up with unit testing in GoogleTest in under 90 seconds
(once you have Bazel installed).

# Use

1. Install [bazel](https://bazel.io)

2. Download the repo: `git clone https://github.com/pyjarrett/absorb_garnish.git my_project`

3. Create a component and its tests. 

```bash
cd my_project/src
../tools/create_component_and_unit_test.py sample
```

4. Run tests:

```bash
bazel test //src:all
```

## What is `create_component_and_unit_test.py`

```bash
usage: create_component_and_unit_test.py component_name
```

A component is a .hpp/.cpp pair, with the test being in
component\_name\_test.cpp.  All three of these get created by this Python file.
An additional rule will be added to the `BUILD` file in that directory as well,
creating `BUILD` if necessary.  If any of the three boilerplate C++ files exist,
no files will get created or overwritten.
