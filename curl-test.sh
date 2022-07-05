#!/bin/bash

# post request
curl --request POST http://localhost:5000/api/timeline_post -d 'name=Emilie&email=emilieyzh@gmail.com&content=Adding a database from bash script to my portfolio site!'

# test post request by checking with GET
curl http://localhost:5000/api/timeline_post

# test delete request with DELETE endpoint
# curl -X DELETE http://localhost:5000/api/timeline_post/<id>