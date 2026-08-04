// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

function Mutex() {
    this.queue = Promise.resolve();
}

Mutex.prototype.run = function(fn) {
    const result = this.queue.then(fn);
    this.queue = result.then(() => {}, () => {}).then(() => {});
    return result;
};

var FizzBuzz = function(n) {
    this.n = n;
    this.current = 1;
    this.mutex = new Mutex();
    this.waiters = [];
};

FizzBuzz.prototype._wait = function() {
    return new Promise((resolve) => {
        this.waiters.push(resolve);
    });
};

FizzBuzz.prototype._notifyAll = function() {
    const pending = this.waiters;
    this.waiters = [];
    pending.forEach((resolve) => resolve());
};

FizzBuzz.prototype._run = async function(predicate, action) {
    while (true) {
        let shouldWait = false;
        let finished = false;
        await this.mutex.run(async () => {
            if (this.current > this.n) {
                finished = true;
                return;
            }
            if (predicate(this.current)) {
                action();
                this.current += 1;
                this._notifyAll();
            } else {
                shouldWait = true;
            }
        });
        if (finished) {
            break;
        }
        if (shouldWait) {
            await this._wait();
        }
    }
};

FizzBuzz.prototype.fizz = async function(printFizz) {
    await this._run((x) => x % 3 === 0 && x % 5 !== 0, printFizz);
};

FizzBuzz.prototype.buzz = async function(printBuzz) {
    await this._run((x) => x % 5 === 0 && x % 3 !== 0, printBuzz);
};

FizzBuzz.prototype.fizzbuzz = async function(printFizzBuzz) {
    await this._run((x) => x % 15 === 0, printFizzBuzz);
};

FizzBuzz.prototype.number = async function(printNumber) {
    await this._run((x) => x % 3 !== 0 && x % 5 !== 0, () => printNumber(this.current));
};
