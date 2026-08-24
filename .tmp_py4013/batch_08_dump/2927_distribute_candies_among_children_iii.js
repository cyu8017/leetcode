// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

/**
 * @param {number} n
 * @param {number} limit
 * @return {number}
 */
var distributeCandies = function(n, limit) {
    const comb = (x) => {
        if (x < 2) return 0;
        return x * (x - 1) / 2;
    };
    let ans = comb(n + 2);
    ans -= 3 * comb(n - limit + 1);
    ans += 3 * comb(n - 2 * (limit + 1) + 2);
    ans -= comb(n - 3 * (limit + 1) + 2);
    if (ans < 0) ans = 0;
    return ans;
};
