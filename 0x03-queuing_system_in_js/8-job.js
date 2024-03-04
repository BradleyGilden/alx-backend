const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (const job of jobs) {
    const notification = queue.create('push_notification_code_2', job).save((err) => {
    console.log(`Notification job created: ${notification.id}`);
    });
  
    notification.on('complete', () => {
      console.log(`Notification job ${notification.id} completed`);
    }).on('failed', (err) => {
      console.log(`Notification job ${notification.id} failed: ${err}`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${notification.id} ${progress}% complete`)
    });
  }
};

export default createPushNotificationsJobs;
