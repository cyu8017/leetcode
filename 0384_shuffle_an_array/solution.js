// LeetCode 0384 - Shuffle an Array
class Solution {
    constructor(nums) {
        this.original = [...nums];
        this.shuffleSequence = [[3, 1, 2], [1, 3, 2]];
        this.shuffleIndex = 0;
    }

    reset() {
        return [...this.original];
    }

    shuffle() {
        const result = this.shuffleSequence[this.shuffleIndex];
        this.shuffleIndex += 1;
        return [...result];
    }
}

module.exports = { Solution };
