// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

function trimMean(arr: number[]): number {
    arr.sort((a, b) => a - b);
    const k = Math.floor(arr.length / 20);
    let sum = 0;
    for (let i = k; i < arr.length - k; i++) sum += arr[i];
    return sum / (arr.length - 2 * k);
}
