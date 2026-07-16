// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

let uniform = () => 0;

function setUniform(uniformFn) {
    uniform = uniformFn;
}

function set_uniform(uniformFn) {
    uniform = uniformFn;
}

class Solution {
    constructor(m, n) {
        this.cols = n;
        this.total = m * n;
        this.reset();
    }

    flip() {
        let index = Math.trunc(uniform(0, this.available.length - 1));
        if (index >= this.available.length) index = this.available.length - 1;
        const value = this.available[index];
        this.available[index] = this.available[this.available.length - 1];
        this.available.pop();
        return [Math.floor(value / this.cols), value % this.cols];
    }

    reset() {
        this.available = Array.from({ length: this.total }, (_, i) => i);
    }
}

module.exports = { Solution, setUniform, set_uniform };
