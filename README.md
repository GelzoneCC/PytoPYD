# PytoPYD
Use Cython to convert .pyx to .pyd.<br>
Build .pyx file which some functions in it and convert it to .pyd so that you can use this .pyd with other .py file.
## Steps
1. Build .pyx file for some common function.
2. Build setup.py for .pyd generation.
3. Command `python setup.py build_ext --inplace` in your .pyx path.
4. Generate .pyd file and then rename it to use.
