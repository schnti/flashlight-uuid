def results(fields, original_query):
	import uuid
    x = uuid.uuid4()
    s = str(x)
    return {
        "title": "UUID",
        "run_args": [s],
	    "html": s
    }

def run(text):
	from AppKit import NSPasteboard, NSPasteboardTypeString
	NSPasteboard.generalPasteboard().clearContents()
	NSPasteboard.generalPasteboard().setString_forType_(text, NSPasteboardTypeString)