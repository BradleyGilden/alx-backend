import kue from 'kue';

const queue = kue.createQueue();

jobData = {
  phoneNumber: string,
  message: string,
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
