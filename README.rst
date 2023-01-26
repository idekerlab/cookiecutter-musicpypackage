======================================
Cookiecutter Idekerlab Python Package
======================================


Cookiecutter_ template for Idekerlab Python packages. This template includes
a command line script and an example class under the ``runner`` module


* Derived from the excellent cookie cutter template: https://github.com/audreyr/cookiecutter

.. _Cookiecutter: https://github.com/audreyr/cookiecutter


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/idekerlab/cookiecutter-cd.git

Then:

* Create a repo and put it there.
* Install the dev requirements into conda or virtualenv environment. (``pip install -r requirements_dev.txt``)
* Test your docs by running ``make docs``
* Edit ``requirements.txt`` and ``setup.py`` files to specify the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Add the repo to your Travis-CI_ account.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Create ``~/.pypirc`` file in your home directory and put the following content in it with your PyPi_ and TestPyPi_ account credentials

.. code-block::

    [distutils]
    index-servers=
    pypi
    testpypi

    [testpypi]
    repository:https://test.pypi.org/legacy/
    username = <TEST PYPI USERNAME>
    password = <TEST PYPI PASSWORD>

    [pypi]
    username:<PYPI USERNAME>
    password:<PYPI PASSWORD>

.. warning::
    DO NOT PUT ``~/.pypirc`` in repo, it should be in your home directory
    with only you having read access

* Release your package to test pypi by running: ``make testrelease``
* Release your package to pypi by running: ``make release``

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/distributing/#register-your-project

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _Punch: https://github.com/lgiordani/punch
.. _PyPi: https://pypi.org
.. _TestPyPi: https://test.pypi.org


.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _`lgiordani/cookiecutter-pypackage`: https://github.com/lgiordani/cookiecutter-pypackage
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
