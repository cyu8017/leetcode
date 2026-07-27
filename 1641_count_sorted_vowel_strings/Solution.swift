// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution {
    func countVowelStrings(_ n: Int) -> Int {
        // C(n+4, 4)
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) / 24
    }
}
