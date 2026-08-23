// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var closestToTarget = function(arr, target) {
    let answer = Infinity;
    let current = new Set();
    for (const value of arr) {
        const next = new Set([value]);
        for (const previous of current) next.add(value & previous);
        current = next;
        for (const candidate of current) answer = Math.min(answer, Math.abs(candidate - target));
    }
    return answer;
};
