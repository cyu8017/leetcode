// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/
// @ts-nocheck

function getIndex(reader: any | number[]): number {
    if (Array.isArray(reader)) {
        const arr = reader;
        reader = {
            compareSub(l, r, x, y) {
                let a = 0, b = 0;
                for (let i = l; i <= r; i++) a += arr[i];
                for (let i = x; i <= y; i++) b += arr[i];
                return a > b ? 1 : a < b ? -1 : 0;
            },
            length() { return arr.length; }
        };
    }
    let left = 0, right = reader.length() - 1;
    while (left < right) {
        const length = right - left + 1;
        const half = Math.floor(length / 2);
        const result = reader.compareSub(left, left + half - 1, right - half + 1, right);
        if (result === 0) return left + half;
        if (result > 0) right = left + half - 1;
        else left = right - half + 1;
    }
    return left;
}
