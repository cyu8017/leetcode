// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

let uniform = () => 0;

function setUniform(uniformFn) {
    uniform = uniformFn;
}

function set_uniform(uniformFn) {
    uniform = uniformFn;
}

class Solution {
    constructor(w) {
        this.prefix = [];
        let total = 0;
        for (const weight of w) {
            total += weight;
            this.prefix.push(total);
        }
        this.total = total;
    }

    pickIndex() {
        let target = Math.trunc(uniform(0, this.total));
        if (target >= this.total) target = this.total - 1;
        let low = 0;
        let high = this.prefix.length - 1;
        while (low < high) {
            const mid = Math.floor((low + high) / 2);
            if (this.prefix[mid] <= target) low = mid + 1;
            else high = mid;
        }
        return low;
    }
}

module.exports = { Solution, setUniform, set_uniform };
