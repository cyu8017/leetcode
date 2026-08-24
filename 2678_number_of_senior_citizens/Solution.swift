// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

class Solution {
    func countSeniors(_ details: [String]) -> Int {
        var ans = 0
        for d in details {
            let chars = Array(d)
            let age = Int(String(chars[11]))! * 10 + Int(String(chars[12]))!
            if age > 60 { ans += 1 }
        }
        return ans
    }
}
