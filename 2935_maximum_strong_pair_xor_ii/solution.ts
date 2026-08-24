// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

export function maximumStrongPairXor(nums: number[]): number {
    nums = [...nums].sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        for (let j = i; j < nums.length && nums[j] <= 2 * x; j++) {
            const xorr = x ^ nums[j];
            if (xorr > ans) ans = xorr;
        }
    }
    return ans;
}
