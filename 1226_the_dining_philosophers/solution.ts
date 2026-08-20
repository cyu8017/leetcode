// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

class DiningPhilosophers {
    locks: Promise<void>[];

    constructor() {
        this.locks = Array.from({ length: 5 }, () => Promise.resolve());
    }

    async wantsToEat(
        philosopher: number,
        pickLeftFork: () => void,
        pickRightFork: () => void,
        eat: () => void,
        putLeftFork: () => void,
        putRightFork: () => void,
    ): Promise<void> {
        const left = philosopher;
        const right = (philosopher + 1) % 5;
        const [first, second] = philosopher % 2 === 0 ? [left, right] : [right, left];
        await (this.locks[first] = this.locks[first].then(pickLeftFork));
        await (this.locks[second] = this.locks[second].then(pickRightFork));
        eat();
        putLeftFork();
        putRightFork();
        this.locks[first] = Promise.resolve();
        this.locks[second] = Promise.resolve();
    }
}
