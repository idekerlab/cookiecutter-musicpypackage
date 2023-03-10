#! /usr/bin/env python

import logging


logger = logging.getLogger(__name__)


class {{ cookiecutter.__runner_class_name }}(object):
    """
    Class to run algorithm
    """
    def __init__(self, exitcode):
        """
        Constructor

        :param exitcode: value to return via :py:meth:`.{{ cookiecutter.__runner_class_name }}.run` method
        :type int:
        """
        self._exitcode = exitcode
        logger.debug('In constructor')

    def run(self):
        """
        Runs {{ cookiecutter.project_name }}


        :return:
        """
        logger.debug('In run method')
        return self._exitcode
