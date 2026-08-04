// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

/**
 * @param {number[]} calories
 * @param {number} k
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var dietPlanPerformance = function(calories, k, lower, upper) {
    let window = 0;
    for (let i = 0; i < k; i++) window += calories[i];
    let ans = 0;
    if (window < lower) ans--;
    else if (window > upper) ans++;
    for (let i = k; i < calories.length; i++) {
        window += calories[i] - calories[i - k];
        if (window < lower) ans--;
        else if (window > upper) ans++;
    }
    return ans;
};
