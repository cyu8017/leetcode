// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

/**
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(cost) {
    const arr = cost.slice().sort((a, b) => b - a);
    let ans = 0;
    for (let i = 0; i < arr.length; i++)
        if (i % 3 !== 2) ans += arr[i];
    return ans;
};
