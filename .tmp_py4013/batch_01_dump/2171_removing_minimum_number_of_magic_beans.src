// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

/**
 * @param {number[]} beans
 * @return {number}
 */
var minimumRemoval = function(beans) {
    beans = beans.slice().sort((a, b) => a - b);
    const n = beans.length;
    let sum = 0;
    for (const b of beans) sum += b;
    let ans = sum;
    for (let i = 0; i < n; i++) {
        const remain = (n - i) * beans[i];
        ans = Math.min(ans, sum - remain);
    }
    return ans;
};
