// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

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

var ZeroEvenOdd = function(n) {
    this.n = n;
    this.zeroSem = new Semaphore(1);
    this.evenSem = new Semaphore(0);
    this.oddSem = new Semaphore(0);
};

ZeroEvenOdd.prototype.zero = async function(printNumber) {
    for (let i = 0; i < this.n; i += 1) {
        await this.zeroSem.acquire();
        printNumber(0);
        if (i % 2 === 0) {
            this.oddSem.release();
        } else {
            this.evenSem.release();
        }
    }
};

ZeroEvenOdd.prototype.even = async function(printNumber) {
    for (let num = 2; num <= this.n; num += 2) {
        await this.evenSem.acquire();
        printNumber(num);
        this.zeroSem.release();
    }
};

ZeroEvenOdd.prototype.odd = async function(printNumber) {
    for (let num = 1; num <= this.n; num += 2) {
        await this.oddSem.acquire();
        printNumber(num);
        this.zeroSem.release();
    }
};
