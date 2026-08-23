// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleDivisorTriplet = function(nums) {
    const freq = new Array(101).fill(0);
    for (const x of nums) freq[x]++;
    let ans = 0;
    for (let a = 1; a <= 100; a++) {
        if (!freq[a]) continue;
        for (let b = a; b <= 100; b++) {
            if (!freq[b]) continue;
            for (let c = b; c <= 100; c++) {
                if (!freq[c]) continue;
                const s = a + b + c;
                let cnt = 0;
                if (s % a === 0) cnt++;
                if (s % b === 0) cnt++;
                if (s % c === 0) cnt++;
                if (cnt !== 1) continue;
                if (a === b && b === c) ans += freq[a] * (freq[a] - 1) * (freq[a] - 2);
                else if (a === b) ans += freq[a] * (freq[a] - 1) * freq[c] * 3;
                else if (b === c) ans += freq[b] * (freq[b] - 1) * freq[a] * 3;
                else if (a === c) ans += freq[a] * (freq[a] - 1) * freq[b] * 3;
                else ans += freq[a] * freq[b] * freq[c] * 6;
            }
        }
    }
    return ans;
};
