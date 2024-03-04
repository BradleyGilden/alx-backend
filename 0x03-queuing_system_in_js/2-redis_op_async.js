import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${String(err)}`));

client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (_err, reply) => {
    print(`Reply: ${reply}`)
  })
}

const displaySchoolValue = async (schoolName) => {
  const getPromise = promisify(client.get).bind(client);
  const reply = await getPromise(schoolName);
  console.log(reply);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
