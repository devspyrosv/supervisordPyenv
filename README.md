# SupervisordPyenv

Run python apps with custom python version using supervisord.

Two possible means of execution are presented.

* Through an intermediate bash script (start_daemon.sh), fed to supervisord's command arg.
* Through a one liner fed to supervisord's command arg.

## Create virtual environment

```bash
pyenv install 3.7.2
pyenv virtualenv 3.7.2 daemon_372
```

## Get supervisord confs ready
In 
 * direct_python_supervisord.conf
 * intermediate_script_supervisord.conf
 
Replace:
```bash 
 * {{ PATH_TO_VIRTUAL_ENVIRONMENT }} -> path to venv (usually ~/.pyenv/versions - expanded) 
 * {{ WORK_DIRECTORY }} -> in case you want the program to run in a certain directory
 * {{ PATH_TO_LOG_DIR }} -> where to place log files
 * {{ USER_NAME_TO_RUN_AS }} -> your username 
 * {{ PATH_TO_PROJECT }} -> where is the project located
```

## Next steps

 * Move the app supervisord conf you would like to test to the conf.d dir of your supervisord installation.
 
 * Use supervisorctl to reread and update the confs.
 
 * Check the log files for successful execution. 


[MIT](https://choosealicense.com/licenses/mit/)