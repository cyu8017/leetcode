// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

export function missingMultiple(nums: any, k: any): any {
    const s = new Set(nums);
    for (let i = 1; ; i++) {
        const x = k * i;
        if (!s.has(x)) return x;
    }
}
