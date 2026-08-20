// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

class Solution {
    func containsPattern(_ arr: [Int], _ m: Int, _ k: Int) -> Bool {
        var run = 0
        for i in m..<arr.count {
            run = arr[i] == arr[i - m] ? run + 1 : 0
            if run >= m * (k - 1) { return true }
        }
        return false
    }
}
