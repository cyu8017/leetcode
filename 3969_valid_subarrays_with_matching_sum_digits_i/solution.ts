// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

export function countValidSubarrays(nums: any, x: any): any {
    const n = nums.length;
    let ans = 0;
    for (let l = 0; l < n; l++) {
        let s = 0;
        for (let r = l; r < n; r++) {
            s += nums[r];
            if (s % 10 === x) {
                const t = String(s);
                if (t.charCodeAt(0) - 48 === x) ans++;
            }
        }
    }
    return ans;
}
