// LeetCode 1449 - Form Largest Integer With Digits That Add up to Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

class Solution {
    func largestNumber(_ cost: [Int], _ target: Int) -> String {
        var dp = Array(repeating: Optional<String>.none, count: target + 1)
        dp[0] = ""
        for total in 1...target {
            var best: String? = nil
            for digit in 1...9 {
                let price = cost[digit - 1]
                if total >= price, let prev = dp[total - price] {
                    let candidate = String(digit) + prev
                    if best == nil || candidate.count > best!.count || (candidate.count == best!.count && candidate > best!) {
                        best = candidate
                    }
                }
            }
            dp[total] = best
        }
        return dp[target] ?? "0"
    }
}
