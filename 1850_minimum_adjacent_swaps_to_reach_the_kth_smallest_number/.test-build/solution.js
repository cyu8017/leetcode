"use strict";
// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
function getMinSwaps(num, k) {
    const nextPermutation = (arr) => {
        let i = arr.length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1])
            i -= 1;
        if (i < 0) {
            arr.reverse();
            return;
        }
        let j = arr.length - 1;
        while (arr[j] <= arr[i])
            j -= 1;
        [arr[i], arr[j]] = [arr[j], arr[i]];
        let l = i + 1, r = arr.length - 1;
        while (l < r) {
            [arr[l], arr[r]] = [arr[r], arr[l]];
            l += 1;
            r -= 1;
        }
    };
    const target = num.split('');
    for (let t = 0; t < k; t++)
        nextPermutation(target);
    const source = num.split('');
    let swaps = 0;
    for (let i = 0; i < source.length; i++) {
        if (source[i] === target[i])
            continue;
        let j = i;
        while (source[j] !== target[i])
            j += 1;
        while (j > i) {
            [source[j], source[j - 1]] = [source[j - 1], source[j]];
            swaps += 1;
            j -= 1;
        }
    }
    return swaps;
}
