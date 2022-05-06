echo “Stopping”

CNT=`ps -ef | grep python | grep mecab_api.py | grep -v grep | wc -l`
PID=`ps -ef | grep python | grep mecab_api.py | grep -v grep | awk '{print $2}'`


if [ $CNT -ne 0 ]
then
        echo "Stop..."
        kill -9 $PID
fi

echo “Stopped”
