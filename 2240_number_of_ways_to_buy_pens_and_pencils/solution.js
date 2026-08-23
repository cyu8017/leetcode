// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

/**
 * @param {number} total
 * @param {number} cost1
 * @param {number} cost2
 * @return {number}
 */
var waysToBuyPensPencils = function(total, cost1, cost2) {
    let ans = 0;
    for (let pens = 0; pens * cost1 <= total; pens++) {
        const remain = total - pens * cost1;
        ans += Math.floor(remain / cost2) + 1;
    }
    return ans;
};
