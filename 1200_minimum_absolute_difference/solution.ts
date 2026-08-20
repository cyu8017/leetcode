// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

function minimumAbsDifference(arr: number[]): number[][] {
    arr.sort((a, b) => a - b);
    let best = Infinity;
    for (let i = 0; i < arr.length - 1; i++) best = Math.min(best, arr[i + 1] - arr[i]);
    const ans = [];
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i + 1] - arr[i] === best) ans.push([arr[i], arr[i + 1]]);
    }
    return ans;
}
