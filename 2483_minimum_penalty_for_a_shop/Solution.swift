// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution {
    func bestClosingTime(_ customers: String) -> Int {
        let chars = Array(customers)
        var penalty = chars.filter { $0 == "Y" }.count
        var best = penalty, ans = 0
        for i in 0..<chars.count {
            if chars[i] == "Y" { penalty -= 1 }
            else { penalty += 1 }
            if penalty < best {
                best = penalty
                ans = i + 1
            }
        }
        return ans
    }
}
