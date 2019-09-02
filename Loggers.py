import logging
from logging.handlers import RotatingFileHandler

class FileRotationLogger(object):  

    """    
    Log Levels:     
    50 (Critical)  - logger.critical(msg)    
    40 (Error)     - logger.error(msg)    
    30 (Warning)   - logger.warning(msg)    
    20 (Info)      - logger.info(msg)    
    10 (Debug)     - logger.debug(msg)    
    0 (Notset)    
    """    

    def __init__(self, logger_name, log_level, file_path, file_size_in_mb, file_count):
        format_ = '%(asctime)-15s %(name)s %(levelname)s %(message)s'
        logging.basicConfig(format=format_, level=log_level)
        self.logger = logging.getLogger(logger_name)
        formatter = logging.Formatter(format_)
        self.file_handler = RotatingFileHandler(file_path, maxBytes=file_size_in_mb*1024*1024, backupCount=file_count)
        self.file_handler.setFormatter(formatter)
        self.file_handler.setLevel(log_level)
        self.logger.addHandler(self.file_handler)

    def get(self):
        return self.logger


if __name__ == "__main__":
    logger = RotatingLogger(logger_name="main_logger", log_level=30, file_path="test.log", file_size_in_mb=10, file_count=5).get()
    logger.warning("Hello World!")
