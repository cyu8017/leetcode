// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var minOperations = function(nums, target) {
    const cnt = Array(32).fill(0);
    let sum = 0;
    for (const v of nums) {
        sum += v;
        let b = 0;
        while ((1 << b) < v) b++;
        cnt[b]++;
    }
    if (sum < target) return -1;
    let ans = 0;
    for (let i = 0; i < 31; i++) {
        if ((target & (1 << i)) !== 0) {
            if (cnt[i] > 0) cnt[i]--;
            else {
                let j = i + 1;
                while (j < 32 && cnt[j] === 0) j++;
                if (j === 32) return -1;
                while (j > i) {
                    cnt[j]--;
                    cnt[j - 1] += 2;
                    ans++;
                    j--;
                }
                cnt[i]--;
            }
        }
        cnt[i + 1] += Math.floor(cnt[i] / 2);
    }
    return ans;
};
