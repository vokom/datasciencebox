{%- from 'cdh5/hdfs/settings.sls' import namenode_fqdn, namenode_dirs, datanode_dirs with context %}

/etc/hadoop/conf:
  file.recurse:
    - source: salt://cdh5/etc/hadoop/conf
    - template: jinja
    - user: root
    - group: root
    - file_mode: 644
    - context:
      namenode_fqdn: {{ namenode_fqdn }}
      namenode_dirs: {{ namenode_dirs }}
      datanode_dirs: {{ datanode_dirs }}
