// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

class Solution {
    func minCharacters(_ a: String, _ b: String) -> Int {
        var ca = [Int](repeating: 0, count: 26)
        var cb = [Int](repeating: 0, count: 26)
        for byte in a.utf8 {
            ca[Int(byte) - 97] += 1
        }
        for byte in b.utf8 {
            cb[Int(byte) - 97] += 1
        }
        let n = a.count
        let m = b.count
        let maxCount = max(ca.max()!, cb.max()!)
        var ans = n + m - maxCount
        var preA = 0
        var preB = 0
        for code in 0..<25 {
            preA += ca[code]
            preB += cb[code]
            ans = min(ans, n - preA + preB, m - preB + preA)
        }
        return ans
    }
}
