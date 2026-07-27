// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

function minMoves(nums: number[], limit: number): number {
    const n = nums.length;
    const d = Array(2 * limit + 2).fill(0);
    for (let i = 0; i < n / 2; i++) {
        const a = nums[i], b = nums[n - 1 - i];
        const lo = Math.min(a, b) + 1;
        const hi = Math.max(a, b) + limit;
        const s = a + b;
        d[2] += 2;
        d[lo] -= 1;
        d[s] -= 1;
        d[s + 1] += 1;
        d[hi + 1] += 1;
    }
    let ans = 1e9, cur = 1e9;
    for (let s = 2; s <= 2 * limit; s++) {
        cur += cur !== 1e9 ? d[s] : d[s] - 1e9;
        ans = Math.min(ans, cur);
    }
    return ans;
}
