// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

/**
 * @param {number[]} chargeTimes
 * @param {number[]} runningCosts
 * @param {number} budget
 * @return {number}
 */
var maximumRobots = function(chargeTimes, runningCosts, budget) {
    const n = chargeTimes.length;
    let left = 0;
    let sum = 0;
    const dq = [];
    let ans = 0;
    for (let right = 0; right < n; right++) {
        while (dq.length > 0 && chargeTimes[dq[dq.length - 1]] <= chargeTimes[right]) dq.pop();
        dq.push(right);
        sum += runningCosts[right];
        while (left <= right && chargeTimes[dq[0]] + (right - left + 1) * sum > budget) {
            if (dq[0] === left) dq.shift();
            sum -= runningCosts[left];
            left++;
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
};
