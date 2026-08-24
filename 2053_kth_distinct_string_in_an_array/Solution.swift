// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution {
    func kthDistinct(_ arr: [String], _ k: Int) -> String {
        var freq = [String: Int]()
        for s in arr { freq[s, default: 0] += 1 }
        var k = k
        for s in arr where freq[s] == 1 {
            k -= 1
            if k == 0 { return s }
        }
        return ""
    }
}
