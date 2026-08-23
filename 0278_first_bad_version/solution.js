// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    firstBadVersion(n) {
        let left = 1;
        let right = n;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (this.isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}

/**
 * @param {number} version
 * @return {boolean}
 */
function isBadVersion(version) {
    return false;
}

module.exports = {
    isBadVersion,
    firstBadVersion: Solution.prototype.firstBadVersion,
    Solution,
};
