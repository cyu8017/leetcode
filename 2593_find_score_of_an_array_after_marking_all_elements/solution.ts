// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

export function findScore(nums: number[]): number {
    const n = nums.length;
    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => nums[a] !== nums[b] ? nums[a] - nums[b] : a - b);
    const marked = new Array(n).fill(false);
    let ans = 0;
    for (const i of idx) {
        if (marked[i]) continue;
        ans += nums[i];
        marked[i] = true;
        if (i - 1 >= 0) marked[i - 1] = true;
        if (i + 1 < n) marked[i + 1] = true;
    }
    return ans;
}
