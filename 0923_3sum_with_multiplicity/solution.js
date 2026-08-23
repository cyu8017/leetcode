// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var threeSumMulti = function(arr, target) {
    const MOD = 1000000007;
    const count = new Array(101).fill(0);
    for (const x of arr) count[x]++;
    let ans = 0;
    for (let a = 0; a <= 100; a++) if (count[a] > 0) {
        for (let b = a; b <= 100; b++) if (count[b] > 0) {
            const c = target - a - b;
            if (c < b || c > 100 || count[c] === 0) continue;
            if (a === b && b === c) ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6;
            else if (a === b) ans += count[a] * (count[a] - 1) / 2 * count[c];
            else if (b === c) ans += count[a] * count[b] * (count[b] - 1) / 2;
            else ans += count[a] * count[b] * count[c];
        }
    }
    return ans % MOD;
};
