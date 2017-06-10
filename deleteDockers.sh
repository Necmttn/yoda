for i in `docker ps -a | grep app.py | awk '{print $1}'`; do docker rm -f $i;done; > deleteDockers.sh
