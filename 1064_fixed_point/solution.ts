// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

function fixedPoint(arr: number[]): number {
    let lo = 0;
    let hi = arr.length - 1;
    let ans = -1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid] === mid) {
            ans = mid;
            hi = mid - 1;
        } else if (arr[mid] < mid) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ans;
}
