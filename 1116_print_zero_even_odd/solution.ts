// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

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

class ZeroEvenOdd {
    n: number;
    zeroSem: Semaphore;
    evenSem: Semaphore;
    oddSem: Semaphore;

    constructor(n: number) {
        this.n = n;
        this.zeroSem = new Semaphore(1);
        this.evenSem = new Semaphore(0);
        this.oddSem = new Semaphore(0);
    }

    async zero(printNumber: (n: number) => void): Promise<void> {
        for (let i = 0; i < this.n; i += 1) {
            await this.zeroSem.acquire();
            printNumber(0);
            if (i % 2 === 0) {
                this.oddSem.release();
            } else {
                this.evenSem.release();
            }
        }
    }

    async even(printNumber: (n: number) => void): Promise<void> {
        for (let num = 2; num <= this.n; num += 2) {
            await this.evenSem.acquire();
            printNumber(num);
            this.zeroSem.release();
        }
    }

    async odd(printNumber: (n: number) => void): Promise<void> {
        for (let num = 1; num <= this.n; num += 2) {
            await this.oddSem.acquire();
            printNumber(num);
            this.zeroSem.release();
        }
    }
}
