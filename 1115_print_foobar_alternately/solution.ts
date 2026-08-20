// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

class Semaphore {
    count: number;
    waiters: Array<() => void>;

    constructor(count: number) {
        this.count = count;
        this.waiters = [];
    }

    acquire(): Promise<void> {
        if (this.count > 0) {
            this.count -= 1;
            return Promise.resolve();
        }
        return new Promise((resolve) => this.waiters.push(resolve));
    }

    release(): void {
        if (this.waiters.length > 0) {
            this.waiters.shift()!();
        } else {
            this.count += 1;
        }
    }
}

class FooBar {
    n: number;
    fooSem: Semaphore;
    barSem: Semaphore;

    constructor(n: number) {
        this.n = n;
        this.fooSem = new Semaphore(1);
        this.barSem = new Semaphore(0);
    }

    async foo(printFoo: () => void): Promise<void> {
        for (let i = 0; i < this.n; i += 1) {
            await this.fooSem.acquire();
            printFoo();
            this.barSem.release();
        }
    }

    async bar(printBar: () => void): Promise<void> {
        for (let i = 0; i < this.n; i += 1) {
            await this.barSem.acquire();
            printBar();
            this.fooSem.release();
        }
    }
}
