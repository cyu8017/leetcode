// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) {
            return 0;
        }

        int needleLen = needle.length();
        for (int i = 0; i <= haystack.length() - needleLen; i++) {
            if (haystack.startsWith(needle, i)) {
                return i;
            }
        }

        return -1;
    }
}
