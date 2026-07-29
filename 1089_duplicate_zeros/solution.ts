// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

function duplicateZeros(arr: number[]): void {
    let zeros = 0;
    for (const x of arr) if (x === 0) zeros++;
    const n = arr.length;
    for (let i = n - 1; i >= 0; i--) {
        if (i + zeros < n) arr[i + zeros] = arr[i];
        if (arr[i] === 0) {
            zeros--;
            if (i + zeros < n) arr[i + zeros] = 0;
        }
    }
}
