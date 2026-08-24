// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution {
    func longestCommonPrefix(_ arr1: [Int], _ arr2: [Int]) -> Int {
        var s = Set<Int>()
        for x0 in arr1 {
            var x = x0
            while x > 0 {
                s.insert(x)
                x /= 10
            }
        }
        var mx = 0
        for x0 in arr2 {
            var x = x0
            while x > 0 {
                if s.contains(x) {
                    mx = max(mx, x)
                    break
                }
                x /= 10
            }
        }
        return mx > 0 ? String(mx).count : 0
    }
}
