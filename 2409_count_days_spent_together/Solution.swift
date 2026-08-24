// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

class Solution {
    func countDaysTogether(_ arriveAlice: String, _ leaveAlice: String, _ arriveBob: String, _ leaveBob: String) -> Int {
        let days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        func toDay(_ s: String) -> Int {
            let a = Array(s)
            let m = Int(String(a[0]))! * 10 + Int(String(a[1]))!
            let d = Int(String(a[3]))! * 10 + Int(String(a[4]))!
            var res = d
            if m > 1 {
                for i in 0..<(m - 1) { res += days[i] }
            }
            return res
        }
        let start = max(toDay(arriveAlice), toDay(arriveBob))
        let end = min(toDay(leaveAlice), toDay(leaveBob))
        return end < start ? 0 : end - start + 1
    }
}
