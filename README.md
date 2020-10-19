# Set up

We'll need a few things to install for this section:

- firefox driver
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)

## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

```bash
source venv/bin/activate
cd course_section_10/
python -m behave tests/acceptance
```
