// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/


class Solution {
    func secondsBetweenTimes(_ startTime: String, _ endTime: String) -> Int {
        func toSeconds(_ s: String) -> Int {
            let c = Array(s)
            let h = (Int(String(c[0]))! * 10) + Int(String(c[1]))!
            let m = (Int(String(c[3]))! * 10) + Int(String(c[4]))!
            let sec = (Int(String(c[6]))! * 10) + Int(String(c[7]))!
            return h * 3600 + m * 60 + sec
        }
        return toSeconds(endTime) - toSeconds(startTime)
    }
}
