// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

function carPooling(trips: number[][], capacity: number): boolean {
    const diff = new Array(1001).fill(0);
    for (const [num, start, end] of trips) {
        diff[start] += num;
        diff[end] -= num;
    }
    let cur = 0;
    for (const x of diff) {
        cur += x;
        if (cur > capacity) return false;
    }
    return true;
}
