"use strict";
// LeetCode 1385: Find The Distance Value Between Two Arrays
function findTheDistanceValue(arr1, arr2, d) {
    arr2.sort((a, b) => a - b);
    return arr1.filter((value) => {
        let left = 0, right = arr2.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (arr2[mid] < value)
                left = mid + 1;
            else
                right = mid;
        }
        return (left === arr2.length || Math.abs(arr2[left] - value) > d) && (left === 0 || Math.abs(arr2[left - 1] - value) > d);
    }).length;
}
