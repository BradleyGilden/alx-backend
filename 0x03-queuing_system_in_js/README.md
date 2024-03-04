# Queueing System in JS

## Learning Objectives

* How to run a Redis server on your machine
* How to run simple operations with the Redis client
* How to use a Redis client with Node JS for basic operations
* How to store hash values in Redis
* How to deal with async operations with Redis
* How to use Kue as a queue system
* How to build a basic Express app interacting with a Redis server
* How to the build a basic Express app interacting with a Redis server and queue

## Files

* [dump.rdb](dump.rdb) - redis backup file
* [0-redis_client.js](0-redis_client.js) :
  * It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
  * It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
* [1-redis_op.js](1-redis_op.js) - In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

  Add two functions:

  * setNewSchool:
    * It accepts two arguments schoolName, and value.
    * It should set in Redis the value for the key schoolName
    * It should display a confirmation message using redis.print
  * displaySchoolValue:
    * It accepts one argument schoolName.
    * It should log to the console the value for the key passed as argument
  * At the end of the file, call:
    * displaySchoolValue('Holberton');
    * setNewSchool('HolbertonSanFrancisco', '100');
    * displaySchoolValue('HolbertonSanFrancisco');
* [2-redis_op_async.js](2-redis_op_async.js) -
* []() -
* []() -
* []() -
* []() -
* []() -
