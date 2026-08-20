// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

class Mutex {
    queue: Promise<unknown>;

    constructor() {
        this.queue = Promise.resolve();
    }

    run(fn: () => unknown): Promise<unknown> {
        const result = this.queue.then(fn);
        this.queue = result.then(() => {}, () => {}).then(() => {});
        return result;
    }
}

class FizzBuzz {
    n: number;
    current: number;
    mutex: Mutex;
    waiters: Array<() => void>;

    constructor(n: number) {
        this.n = n;
        this.current = 1;
        this.mutex = new Mutex();
        this.waiters = [];
    }

    _wait(): Promise<void> {
        return new Promise((resolve) => {
            this.waiters.push(resolve);
        });
    }

    _notifyAll(): void {
        const pending = this.waiters;
        this.waiters = [];
        pending.forEach((resolve) => resolve());
    }

    async _run(predicate: (x: number) => boolean, action: () => void): Promise<void> {
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
    }

    async fizz(printFizz: () => void): Promise<void> {
        await this._run((x) => x % 3 === 0 && x % 5 !== 0, printFizz);
    }

    async buzz(printBuzz: () => void): Promise<void> {
        await this._run((x) => x % 5 === 0 && x % 3 !== 0, printBuzz);
    }

    async fizzbuzz(printFizzBuzz: () => void): Promise<void> {
        await this._run((x) => x % 15 === 0, printFizzBuzz);
    }

    async number(printNumber: (n: number) => void): Promise<void> {
        await this._run((x) => x % 3 !== 0 && x % 5 !== 0, () => printNumber(this.current));
    }
}
