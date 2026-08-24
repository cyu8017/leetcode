// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

export function maxDistance(arrays: number[][]): number {
    let minVal = arrays[0][0];
    let maxVal = arrays[0][arrays[0].length - 1];
    let best = 0;
    for (let i = 1; i < arrays.length; ++i) {
        const arr = arrays[i];
        const first = arr[0], last = arr[arr.length - 1];
        best = Math.max(best, Math.abs(last - minVal), Math.abs(maxVal - first));
        minVal = Math.min(minVal, first);
        maxVal = Math.max(maxVal, last);
    }
    return best;
}
