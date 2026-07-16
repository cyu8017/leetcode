// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

function hIndex(citations: number[]): number {
    let left = 0;
    let right = citations.length - 1;
    const length = citations.length;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const papers = length - mid;
        if (citations[mid] >= papers) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return length - left;
}
