include:
  - java
  - cdh5.repo

hive:
  pkg.installed:
    - require:
      - sls: cdh5.repo

/etc/hive/conf/hive-site.xml:
  file.managed:
    - source: salt://cdh5/etc/hive/conf/hive-site.xml
    - template: jinja
    - user: root
    - group: root
    - file_mode: 644
    - require:
      - pkg: hive
