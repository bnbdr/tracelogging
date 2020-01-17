from tracelogging import Provider, event

class PythonProvider(Provider):
    @event() # mind the parentheses
    def BasicEvent(self):
        pass

log = PythonProvider()

# run: EtwConsumer.exe PythonProvider
log.BasicEvent()