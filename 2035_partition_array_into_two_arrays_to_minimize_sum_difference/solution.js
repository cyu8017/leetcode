// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDifference = function(nums) {
    const n = nums.length / 2;
    let total = 0;
    for (const v of nums) total += v;
    const left = nums.slice(0, n);
    const right = nums.slice(n);
    const sumsByCount = (arr) => {
        const m = arr.length;
        const res = Array.from({length: m + 1}, () => []);
        for (let mask = 0; mask < (1 << m); mask++) {
            let sum = 0, c = 0;
            for (let i = 0; i < m; i++) if ((mask & (1 << i)) !== 0) { sum += arr[i]; c++; }
            res[c].push(sum);
        }
        for (const v of res) v.sort((a, b) => a - b);
        return res;
    };
    const L = sumsByCount(left);
    const R = sumsByCount(right);
    let ans = Number.MAX_SAFE_INTEGER;
    for (let k = 0; k <= n; k++) {
        for (const s1 of L[k]) {
            const need = Math.floor(total / 2) - s1;
            const arr = R[n - k];
            let lo = 0, hi = arr.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (arr[mid] < need) lo = mid + 1;
                else hi = mid;
            }
            for (const j of [lo - 1, lo]) {
                if (j >= 0 && j < arr.length) {
                    const s2 = arr[j];
                    ans = Math.min(ans, Math.abs(total - 2 * (s1 + s2)));
                }
            }
        }
    }
    return ans;
};
