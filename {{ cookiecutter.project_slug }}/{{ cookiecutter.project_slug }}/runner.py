#! /usr/bin/env python

import os
import time
import logging
from cellmaps_utils import logutils
from cellmaps_utils.provenance import ProvenanceUtil

import {{ cookiecutter.project_slug }}

logger = logging.getLogger(__name__)


class {{ cookiecutter.__runner_class_name }}(object):
    """
    Class to run algorithm
    """
    def __init__(self, outdir=None,
                 exitcode=None,
                 skip_logging=False,
                 input_data_dict=None):
        """
        Constructor

        :param exitcode: value to return via :py:meth:`.{{ cookiecutter.__runner_class_name }}.run` method
        :type int:
        """
        if outdir is None:
            raise {{ cookiecutter.__error_class_name }}('outdir is None')

        self._outdir = os.path.abspath(outdir)
        self._exitcode = exitcode
        self._start_time = int(time.time())
        self._end_time = -1
        if skip_logging is None:
            self._skip_logging = False
        else:
            self._skip_logging = skip_logging
        self._input_data_dict = input_data_dict
        logger.debug('In constructor')

    def _write_task_start_json(self):
        """
        Writes task_start.json file with information about
        what is to be run

        """
        data = {}

        if self._input_data_dict is not None:
            data.update({'commandlineargs': str(self._input_data_dict)})

        logutils.write_task_start_json(outdir=self._outdir,
                                       start_time=self._start_time,
                                       version={{ cookiecutter.project_slug }}.__version__,
                                       data=data)

    def _create_output_directory(self):
        """
        Creates output directory

        """
        if os.path.isdir(self._outdir):
            raise {{cookiecutter.__error_class_name}}(self._outdir + ' already exists')

        os.makedirs(self._outdir, mode=0o755)

    def run(self):
        """
        Runs {{ cookiecutter.project_name }}


        :return:
        """
        exitcode = 99
        try:
            logger.debug('In run method')
            self._create_output_directory()
            self._write_task_start_json()
            return self._exitcode
        finally:
            self._end_time = int(time.time())
            if self._skip_logging is False:
                # write a task finish file
                logutils.write_task_finish_json(outdir=self._outdir,
                                                start_time=self._start_time,
                                                end_time=self._end_time,
                                                status=exitcode)


        return exitcode
