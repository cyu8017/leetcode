// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

function addRungs(rungs: number[], dist: number): number {
    let prev = 0, ans = 0;
    for (const r of rungs) {
        ans += Math.floor((r - prev - 1) / dist);
        prev = r;
    }
    return ans;
}
