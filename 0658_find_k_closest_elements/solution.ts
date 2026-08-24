// LeetCode 0658 - Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/

export function findClosestElements(arr: number[], k: number, x: number): number[] {
    let left = 0, right = arr.length - k;
    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);
        if (x - arr[mid] > arr[mid + k] - x) left = mid + 1;
        else right = mid;
    }
    return arr.slice(left, left + k);
}
