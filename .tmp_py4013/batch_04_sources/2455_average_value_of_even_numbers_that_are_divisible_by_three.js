// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    let sum = 0, cnt = 0;
    for (const x of nums) {
        if (x % 6 === 0) {
            sum += x;
            cnt++;
        }
    }
    return cnt === 0 ? 0 : Math.floor(sum / cnt);
};
