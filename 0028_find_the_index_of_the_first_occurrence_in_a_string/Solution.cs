// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

public class Solution {
    public int StrStr(string haystack, string needle) {
        if (needle.Length == 0) {
            return 0;
        }

        int needleLen = needle.Length;
        for (int i = 0; i <= haystack.Length - needleLen; i++) {
            if (haystack.Substring(i, needleLen) == needle) {
                return i;
            }
        }

        return -1;
    }
}
