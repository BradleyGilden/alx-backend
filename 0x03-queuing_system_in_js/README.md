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
* [2-redis_op_async.js](2-redis_op_async.js) - In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)
  Using promisify, modify the function displaySchoolValue to use ES6 async / await

* [4-redis_advanced_op.js](4-redis_advanced_op.js) - Create Hash:

  Using hset, let’s store the following:

  * The key of the hash should be HolbertonSchools
  * It should have a value for:
    * Portland=50
    * Seattle=80
    * New York=20
    * Bogota=20
    * Cali=40
    * Paris=2
* [5-*.js](5-subscriber.js) - In a file named 5-subscriber.js, create a redis client:

  * On connect, it should log the message Redis client connected to the server
  * On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
  * It should subscribe to the channel holberton school channel
  * When it receives message on the channel holberton school channel, it should log the message to the console
  * When the message is KILL_SERVER, it should unsubscribe and quit

  In a file named 5-publisher.js, create a redis client:

  * On connect, it should log the message Redis client connected to the server
  * On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
  * Write a function named publishMessage:
    * It will take two arguments: message (string), and time (integer - in ms)
    * After time millisecond:
      * The function should log to the console About to send MESSAGE
      * The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments
* []() -
* []() -
* []() -
