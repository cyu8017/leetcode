// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

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

class H2O {
    hSem: Semaphore;
    oSem: Semaphore;
    count: number;
    mutex: Mutex;

    constructor() {
        this.hSem = new Semaphore(2);
        this.oSem = new Semaphore(0);
        this.count = 0;
        this.mutex = new Mutex();
    }

    async hydrogen(releaseHydrogen: () => void): Promise<void> {
        await this.hSem.acquire();
        await this.mutex.run(async () => {
            this.count += 1;
            if (this.count === 2) {
                this.oSem.release();
            }
        });
        releaseHydrogen();
    }

    async oxygen(releaseOxygen: () => void): Promise<void> {
        await this.oSem.acquire();
        releaseOxygen();
        await this.mutex.run(async () => {
            this.count = 0;
        });
        this.hSem.release();
        this.hSem.release();
    }
}
