cd dist
del /Q /F *
cd ../
py setup.py sdist bdist_wheel