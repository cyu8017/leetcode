// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

function queryString(s: string, n: number): boolean {
    for (let i = n; i > Math.floor(n / 2); i--) {
        if (!s.includes(i.toString(2))) return false;
    }
    return true;
}
