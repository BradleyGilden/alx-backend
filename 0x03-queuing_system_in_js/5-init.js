// Creates processes to initiate the two files to run parallel to one another
import { fork } from 'child_process';

const subscriber = fork('/home/nightlock/.nvm/versions/node/v12.22.12/bin/npm', ['run', 'dev', '5-subscriber.js'], {
  stdio: 'inherit' // Share stdin, stdout, and stderr with the parent process
});

const publisher = fork('/home/nightlock/.nvm/versions/node/v12.22.12/bin/npm', ['run', 'dev', '5-publisher.js'], {
  stdio: 'ignore' // Share stdin, stdout, and stderr with the parent process
});

subscriber.on('error', err => console.log(`Redis client not connected to the server: ${String(err)}`));
publisher.on('error', err => console.log(`Redis client not connected to the server: ${String(err)}`));
