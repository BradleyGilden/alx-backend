import { expect } from 'chai';
import { it, describe } from 'mocha';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';
import kue from 'kue';

const methods = {
  createPushNotificationsJobs,
}


describe('createPushNotificationsJobs', () => {
  // global vars
  let cpnSpy;
  let queue;
  let consoleSpy;

  beforeEach(() => {
    // Create a spy on createPushNotificationsJobs method
    cpnSpy = sinon.spy(methods, 'createPushNotificationsJobs');
    consoleSpy = sinon.spy(console, 'log');
    // Enter test mode before running tests
    queue = kue.createQueue({ name: 'push_notification_code_test' });
    queue.testMode.enter();
  });

  afterEach(() => {
    // Restore the spy after each test
    cpnSpy.restore();
    consoleSpy.restore();
    // Clear the queue after each test
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('throw an error if jobs is not an array', () => {
    const wrongType =
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    }
    const test = () => createPushNotificationsJobs(wrongType, queue);
    expect(test).to.throw(Error, 'Jobs is not an array');
    cpnSpy.calledOnceWith(wrongType);
    cpnSpy.threw();
  });

  it('check if job was created with the right data', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).equal('push_notification_code_2');
    expect(queue.testMode.jobs[0].data).eql(list[0]);
    expect(queue.testMode.jobs[0].id).equal('1')
    expect(queue.testMode.jobs[1].id).equal('2')
    cpnSpy.calledOnceWith(list);
  });

  it('check if job creation logs were executed', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    consoleSpy.calledOnceWith('Notification job created: 1');
    consoleSpy.calledOnceWith('Notification job created: 2');
  });
});
