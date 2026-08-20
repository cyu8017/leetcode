// LeetCode 1534 - Count Good Triplets
// https://leetcode.com/problems/count-good-triplets/
// @ts-nocheck

function countGoodTriplets(arr: number[], a: number, b: number, c: number): number {
    let ans = 0;
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(arr[i] - arr[j]) > a) continue;
            for (let k = j + 1; k < n; k++) {
                if (Math.abs(arr[j] - arr[k]) <= b && Math.abs(arr[i] - arr[k]) <= c) ans++;
            }
        }
    }
    return ans;
}
