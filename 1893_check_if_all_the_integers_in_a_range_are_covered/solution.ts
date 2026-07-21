// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

function isCovered(ranges: number[][], left: number, right: number): boolean {
    const covered = new Array(51).fill(false);
    for (const [start, end] of ranges) {
        for (let v = start; v <= end; v++) covered[v] = true;
    }
    for (let v = left; v <= right; v++) {
        if (!covered[v]) return false;
    }
    return true;
}
