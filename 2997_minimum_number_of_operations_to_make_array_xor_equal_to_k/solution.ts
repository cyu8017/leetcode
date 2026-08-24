// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

export function minOperations(nums: any, k: any): any {
    let xorr = 0;
    for (const v of nums) xorr ^= v;
    let diff = xorr ^ k;
    let ans = 0;
    while (diff > 0) {
        ans += diff & 1;
        diff >>= 1;
    }
    return ans;
}
