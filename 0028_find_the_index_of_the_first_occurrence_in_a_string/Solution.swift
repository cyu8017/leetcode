// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        if needle.isEmpty {
            return 0
        }

        let haystackChars = Array(haystack)
        let needleChars = Array(needle)
        let needleLen = needleChars.count

        for i in 0...(haystackChars.count - needleLen) {
            if Array(haystackChars[i..<(i + needleLen)]) == needleChars {
                return i
            }
        }

        return -1
    }
}
