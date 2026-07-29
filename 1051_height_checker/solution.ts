// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

function heightChecker(heights: number[]): number {
    const sorted = [...heights].sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < heights.length; i++) {
        if (heights[i] !== sorted[i]) ans++;
    }
    return ans;
}
