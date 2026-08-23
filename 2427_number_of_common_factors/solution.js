// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var commonFactors = function(a, b) {
    const gcd = (x, y) => {
        while (y !== 0) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    const g = gcd(a, b);
    let ans = 0;
    for (let i = 1; i * i <= g; i++) {
        if (g % i === 0) {
            ans++;
            if (i * i !== g) ans++;
        }
    }
    return ans;
};
