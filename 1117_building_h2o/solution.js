// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

function Semaphore(count) {
    this.count = count;
    this.waiters = [];
}

Semaphore.prototype.acquire = function() {
    if (this.count > 0) {
        this.count -= 1;
        return Promise.resolve();
    }
    return new Promise((resolve) => this.waiters.push(resolve));
};

Semaphore.prototype.release = function() {
    if (this.waiters.length > 0) {
        this.waiters.shift()();
    } else {
        this.count += 1;
    }
};

function Mutex() {
    this.queue = Promise.resolve();
}

Mutex.prototype.run = function(fn) {
    const result = this.queue.then(fn);
    this.queue = result.then(() => {}, () => {}).then(() => {});
    return result;
};

var H2O = function() {
    this.hSem = new Semaphore(2);
    this.oSem = new Semaphore(0);
    this.count = 0;
    this.mutex = new Mutex();
};

H2O.prototype.hydrogen = async function(releaseHydrogen) {
    await this.hSem.acquire();
    await this.mutex.run(async () => {
        this.count += 1;
        if (this.count === 2) {
            this.oSem.release();
        }
    });
    releaseHydrogen();
};

H2O.prototype.oxygen = async function(releaseOxygen) {
    await this.oSem.acquire();
    releaseOxygen();
    await this.mutex.run(async () => {
        this.count = 0;
    });
    this.hSem.release();
    this.hSem.release();
};
