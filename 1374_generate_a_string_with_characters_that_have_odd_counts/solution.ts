// LeetCode 1374 - Generate A String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

function generateTheString(n: number): string {
    return n % 2 ? "a".repeat(n) : "a".repeat(n - 1) + "b";
}
