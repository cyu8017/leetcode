// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    findCelebrity(n) {
        let candidate = 0;
        for (let person = 1; person < n; person++) {
            if (this.knows(candidate, person)) {
                candidate = person;
            }
        }
        for (let person = 0; person < n; person++) {
            if (person === candidate) {
                continue;
            }
            if (this.knows(candidate, person) || !this.knows(person, candidate)) {
                return -1;
            }
        }
        return candidate;
    }
}

/**
 * @param {number} a
 * @param {number} b
 * @return {boolean}
 */
function knows(a, b) {
    return false;
}

module.exports = {
    knows,
    findCelebrity: Solution.prototype.findCelebrity,
    Solution,
};
