source ~/.bashrc
python3 -m pytest ./tests/testing.py
python3 -m coverage run -m pytest ./tests/testing.py
python3 -m coverage report -m