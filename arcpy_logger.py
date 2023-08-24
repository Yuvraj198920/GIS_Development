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

