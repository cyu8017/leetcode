// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

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

var FooBar = function(n) {
    this.n = n;
    this.fooSem = new Semaphore(1);
    this.barSem = new Semaphore(0);
};

FooBar.prototype.foo = async function(printFoo) {
    for (let i = 0; i < this.n; i += 1) {
        await this.fooSem.acquire();
        printFoo();
        this.barSem.release();
    }
};

FooBar.prototype.bar = async function(printBar) {
    for (let i = 0; i < this.n; i += 1) {
        await this.barSem.acquire();
        printBar();
        this.fooSem.release();
    }
};
