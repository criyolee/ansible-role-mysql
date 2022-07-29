MYSQL DB
========

This roles installs mysql database

Role Variables
--------------

db_name: The name of the database to create

db_user: The database user to create

db_user_password: The password fo the database user

root_user: root

root_password: root password required to connect to the database

Dependencies
------------

Python must be installed.

Python MySQL packages must also be installed

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - mysql_db

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
