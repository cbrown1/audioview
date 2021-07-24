install:
	install -D audioview.py /usr/local/bin/audioview.py
	ln -s /usr/local/bin/audioview.py /usr/local/bin/audioview

uninstall:
	-rm /usr/local/bin/audioview
	-rm /usr/local/bin/audioview.py
