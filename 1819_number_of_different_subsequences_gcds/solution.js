// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countDifferentSubsequenceGCDs = function(nums) {
    const gcd = (a, b) => {
        while (b) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const maxVal = Math.max(...nums);
    const present = new Array(maxVal + 1).fill(false);
    for (const num of nums) present[num] = true;

    let ans = 0;
    for (let g = 1; g <= maxVal; g++) {
        let has = false;
        let gcdVal = 0;
        for (let multiple = g; multiple <= maxVal; multiple += g) {
            if (present[multiple]) {
                has = true;
                gcdVal = gcd(gcdVal, Math.floor(multiple / g));
                if (gcdVal === 1) break;
            }
        }
        if (has && gcdVal === 1) ans += 1;
    }
    return ans;
};
