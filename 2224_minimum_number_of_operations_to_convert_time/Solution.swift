// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution {
    func convertTime(_ current: String, _ correct: String) -> Int {
        func toMin(_ t: String) -> Int {
            let a = Array(t)
            return Int(String(a[0]))! * 600 + Int(String(a[1]))! * 60
                + Int(String(a[3]))! * 10 + Int(String(a[4]))!
        }
        var diff = toMin(correct) - toMin(current)
        var ans = 0
        for step in [60, 15, 5, 1] {
            ans += diff / step
            diff %= step
        }
        return ans
    }
}
