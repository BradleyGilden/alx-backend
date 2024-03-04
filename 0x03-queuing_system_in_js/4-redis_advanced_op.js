import { createClient, print } from 'redis';

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${String(err)}`));

client.on('ready', () => console.log('Redis client connected to the server'));

const hash = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
}

for (const key of Object.keys(hash)) {

  client.hset('HolbertonSchools', key, hash[key], (_err, reply) => {
    print(`Reply: ${reply}`);
  });
}

client.hgetall('HolbertonSchools', (_err, reply) => {
  console.log(reply);
})
