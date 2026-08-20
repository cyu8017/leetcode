// LeetCode 1346 - Check If N And Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

function checkIfExist(arr: number[]): boolean {
    const seen = new Set();
    for (const value of arr) {
        if (seen.has(2 * value) || (value % 2 === 0 && seen.has(value / 2))) return true;
        seen.add(value);
    }
    return false;
}
