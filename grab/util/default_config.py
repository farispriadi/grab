class DefaultConfig(object):
    GRAB_SPIDER_MODULES = ['spider']
    GRAB_SAVE_FATAL_ERRORS = True
    GRAB_SAVE_TASK_ADD_ERRORS = True
    GRAB_SAVE_FINAL_STATS = True
    GRAB_THREAD_NUMBER = 1
    GRAB_NETWORK_TRY_LIMIT = 10
    GRAB_TASK_TRY_LIMIT = 10
    GRAB_DISPLAY_TIMING = True
    GRAB_DISPLAY_STATS = True

default_config = DefaultConfig()