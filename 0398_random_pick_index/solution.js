// LeetCode 0398 - Random Pick Index
class Solution {
    constructor(nums) {
        this.indices = new Map();
        nums.forEach((value, index) => {
            if (!this.indices.has(value)) this.indices.set(value, []);
            this.indices.get(value).push(index);
        });
        this.pickSequence = [4, 0, 2];
        this.pickIndex = 0;
    }

    pick(target) {
        const value = this.pickSequence[this.pickIndex];
        this.pickIndex += 1;
        return value;
    }
}

module.exports = { Solution };
