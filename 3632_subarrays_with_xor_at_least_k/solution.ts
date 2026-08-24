// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

export function subarraysWithXorAtLeastK(nums: any, k: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let x = 0;
        for (let j = i; j < n; j++) {
            x ^= nums[j];
            if (x >= k) ans++;
        }
    }
    return ans;
}
