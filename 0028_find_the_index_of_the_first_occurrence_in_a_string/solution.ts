// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

export function strStr(haystack: string, needle: string): number {
    if (needle.length === 0) {
        return 0;
    }

    const needleLen = needle.length;
    for (let i = 0; i <= haystack.length - needleLen; i++) {
        if (haystack.slice(i, i + needleLen) === needle) {
            return i;
        }
    }

    return -1;
}
