#!/bin/bash
# Test soo basic for education purpose 
# for guest the port is 8080 for the host port is 8082
# By: Franklin A.
if [ $(curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/) == "200" ] ;
then
	echo "HTTP Status Codes: OK" ;
else
	echo "HTTP Status Codes: Faild";
fi

if [ $(curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/todos) == "200" ] ;
then
	echo "HTTP Status Codes: OK" ;
else
	echo "HTTP Status Codes: Faild";
fi

if [ $(curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/todos/1) == "200" ] ;
then
	echo "HTTP Status Codes: OK" ;
else
	echo "HTTP Status Codes: Faild";
fi

if [ $(curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/todos/2) == "200" ] ;
then
	echo "HTTP Status Codes: OK" ;
else
	echo "HTTP Status Codes: Faild";
fi

if [ $(curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/todos/3) == "404" ] ;
then
	echo "HTTP Status Codes: OK" ;
else
	echo "HTTP Status Codes: Faild";
fi
