// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

var DiningPhilosophers = function() {
    this.locks = Array.from({ length: 5 }, () => Promise.resolve());
};

/**
 * @param {number} philosopher
 * @param {function} pickLeftFork
 * @param {function} pickRightFork
 * @param {function} eat
 * @param {function} putLeftFork
 * @param {function} putRightFork
 * @return {Promise<void>}
 */
DiningPhilosophers.prototype.wantsToEat = async function(
    philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork
) {
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
};
