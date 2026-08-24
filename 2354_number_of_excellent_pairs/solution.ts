// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

export function countExcellentPairs(nums: number[], k: number): number {
    const uniq = new Set(nums);
    const cnt = Array(32).fill(0);
    const bitCount = (x) => {
        let c = 0;
        while (x) { x &= x - 1; c++; }
        return c;
    };
    for (const x of uniq) cnt[bitCount(x)]++;
    let ans = 0;
    for (let i = 0; i < 32; i++) {
        for (let j = 0; j < 32; j++) {
            if (i + j >= k) ans += cnt[i] * cnt[j];
        }
    }
    return ans;
}
