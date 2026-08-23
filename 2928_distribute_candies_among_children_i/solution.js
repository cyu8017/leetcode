// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

/**
 * @param {number} n
 * @param {number} limit
 * @return {number}
 */
var distributeCandies = function(n, limit) {
    let ans = 0;
    for (let i = 0; i <= limit; i++)
        for (let j = 0; j <= limit; j++) {
            const k = n - i - j;
            if (k >= 0 && k <= limit) ans++;
        }
    return ans;
};
