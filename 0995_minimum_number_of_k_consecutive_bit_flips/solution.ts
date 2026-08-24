// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

export function minKBitFlips(nums: number[], k: number): number {
    const n = nums.length;
    const flip = new Array(n).fill(0);
    let ans = 0, flipped = 0;
    for (let i = 0; i < n; i++) {
        if (i >= k) flipped ^= flip[i - k];
        if (nums[i] === flipped) {
            if (i + k > n) return -1;
            ans++;
            flipped ^= 1;
            flip[i] = 1;
        }
    }
    return ans;
}
