// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

class Solution {
    func maxSubstrings(_ word: String) -> Int {
        var ans = 0
        var first = [Character: Int]()
        for (i, c) in word.enumerated() {
            if first[c] == nil { first[c] = i }
            else if i - first[c]! + 1 >= 4 {
                ans += 1
                first.removeAll()
            }
        }
        return ans
    }
}
