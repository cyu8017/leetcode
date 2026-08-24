// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

export function sumDivisibleByK(nums: any, k: any): any {
    const cnt = new Map();
    for (const x of nums) cnt.set(x, (cnt.get(x) || 0) + 1);
    let ans = 0;
    for (const [key, val] of cnt) {
        if (val % k === 0) ans += key * val;
    }
    return ans;
}
