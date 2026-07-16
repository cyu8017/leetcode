// LeetCode 0374 - Guess Number Higher or Lower
class Solution {
    guessNumber(n) {
        let left = 1;
        let right = n;
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            const result = this.guess(mid);
            if (result === 0) return mid;
            if (result < 0) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }

    guess(num) {
        return 0;
    }
}

module.exports = {
    Solution,
    guess: Solution.prototype.guess,
    guessNumber: Solution.prototype.guessNumber,
};
