import logging
import logging.handlers

import arcpy

class ArcPyLogHandler(logging.handlers.RotatingFileHandler):
    """
    Custom logging class that bounces messages to the arcpy tool window as well
    as reflecting back to the file.
    """
    
    def emit(self, record):
        try:
            msg = record.msg.format(record.msg)
        except:
            msg = record.msg

        if record.levelno >= logging.error: # type: ignore
            arcpy.AddError(msg)
        
        elif record.levelno >= logging.warning: # type: ignore
            arcpy.AddWarning(msg)
        
        elif record.levelno >= logging.info: # type: ignore
            arcpy.AddMessage(msg)

        super(ArcPyLogHandler, self).emit(record)

logger = logging.getLogger("LoggerName")
handler = ArcPyLogHandler(
        "output_log.log",
        maxBytes=1024 * 1024 * 2, #2MB log files
        backupCount=10
    )
formatter = logging.Formatter("%(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)