from tracelogging import Provider, event, Types, TraceLevel

class PythonProvider(Provider):
    Name = 'Company-Product-Component'

    @event(Name='FileSize', Id=1, Level=TraceLevel.Warning, Keyword=0x01)
    def not_a_nice_event_name(self, file_path:Types.UnicodeString, file_size:Types.UInt32):
        print('this will be called after the event is written, if you wish to implement anything here')

# run: EtwConsumer.exe Company-Product-Component
log = PythonProvider()
log.not_a_nice_event_name('C:\\windows\\system32\\calc.exe', 0x1000) # will send event named 'FileSize'