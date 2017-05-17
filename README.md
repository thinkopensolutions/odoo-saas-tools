odoo-saas-tools
===============

System to sale and manage odoo databases.

Configuration Requirements
==========================

To start SaaS system you need:

Nginx
-----

    server {
        listen 80 default_server;

        proxy_set_header Host $host;
        
        proxy_set_header X-Real-IP       $remote_addr;
        
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        proxy_set_header X-Forwarded-Proto $scheme;

        location /longpolling {
            proxy_pass http://127.0.0.1:8072;
        }

        location / {
            proxy_pass http://127.0.0.1:8069;
        }
    }
    
Databases on /etc/hosts
-----------------------

If you install it locally, or dns records otherwise:

    sudo bash -c "python saas.py --print-local-hosts >> /etc/hosts"

dbfilter
========

``dbfilter`` in config file or ``--db-filter`` parameter in running command must be::

    ^%h$
    
db_name
=======
be sure, that you don't use ``db_name`` in config file and don't run odoo with ``-d`` (``--database``) parameter

workers
=======

Set ``workers`` parameter to ``3`` or above. In some context it could be less, but ``3`` is enough at any case.

limit_time_cpu
==============

Increase this value. Set it 600 or more.

limit_time_real
==============

Increase this value. Set it 1200 or more.

Build and run
=============

Execute saas.py script and wait some time

> python saas.py --portal-create --portal-db-name=odoo.local.com(main database) --server-create --server-db-name=s1.odoo.local.com(server database) --run --odoo-script=/home/[user]/Odoo/odoo100/bin/start_odoo --odoo-config=/home/[user]/Odoo/odoo100/etc/odoo.cfg
