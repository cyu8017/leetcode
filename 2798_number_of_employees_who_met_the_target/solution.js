// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function(hours, target) {
    let ans = 0;
    for (const h of hours) if (h >= target) ans++;
    return ans;
};
