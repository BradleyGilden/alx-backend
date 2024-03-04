// Creates processes to initiate the two files to run parallel to one another
import { fork } from 'child_process';

const creator = fork('/home/nightlock/.nvm/versions/node/v12.22.12/bin/npm', ['run', 'dev', '7-job_creator.js'], {
  stdio: 'inherit' // Share stdin, stdout, and stderr with the parent process
});

const processor = fork('/home/nightlock/.nvm/versions/node/v12.22.12/bin/npm', ['run', 'dev', '7-job_processor.js'], {
  stdio: 'ignore' // Share stdin, stdout, and stderr with the parent process
});

creator.on('error', err => console.log(`Redis client not connected to the server: ${String(err)}`));
processor.on('error', err => console.log(`Redis client not connected to the server: ${String(err)}`));
