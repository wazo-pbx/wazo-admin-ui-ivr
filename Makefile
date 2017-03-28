install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/ivr.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-ivr
	rm /etc/wazo-admin-ui/conf.d/ivr.yml
	systemctl restart wazo-admin-ui
