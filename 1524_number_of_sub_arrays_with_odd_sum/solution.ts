// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
// @ts-nocheck

function numOfSubarrays(arr: number[]): number {
    const counts = [1, 0];
    let parity = 0, answer = 0;
    for (const value of arr) {
        parity ^= value & 1;
        answer += counts[parity ^ 1];
        counts[parity]++;
    }
    return answer % 1000000007;
}
