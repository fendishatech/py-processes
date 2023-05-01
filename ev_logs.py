import win32evtlog

server = 'localhost'
log_type = 'System'
handle = win32evtlog.OpenEventLog(server, log_type)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

while True:
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    if not events:
        break
    for event in events:
        print(f'Event ID: {event.EventID}')
        print(f'Source Name: {event.SourceName}')
        print(f'Time Generated: {event.TimeGenerated}')
        print('---')

win32evtlog.CloseEventLog(handle)