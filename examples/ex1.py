import tracelogging

log = tracelogging.getLogger('MyLoggerName')

# run: EtwConsumer.exe MyLoggerName
log.debug('ging')
log.info('rmation')
log.warning('be careful')
log.error('err')
log.critical('oh no!')