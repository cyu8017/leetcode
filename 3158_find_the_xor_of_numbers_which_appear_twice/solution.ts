// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

export function duplicateNumbersXOR(nums: number[]): number {
    const cnt = new Array(51).fill(0);
    let ans = 0;
    for (const x of nums) {
        if (++cnt[x] === 2) ans ^= x;
    }
    return ans;
}
