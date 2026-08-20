// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    func equalSubstring(_ s: String, _ t: String, _ maxCost: Int) -> Int {
        let a = Array(s), b = Array(t)
        var left = 0, cost = 0, ans = 0
        for right in 0..<a.count {
            cost += abs(Int(a[right].asciiValue!) - Int(b[right].asciiValue!))
            while cost > maxCost {
                cost -= abs(Int(a[left].asciiValue!) - Int(b[left].asciiValue!))
                left += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
