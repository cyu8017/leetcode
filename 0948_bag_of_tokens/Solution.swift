// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

class Solution {
    func bagOfTokensScore(_ tokens: [Int], _ power: Int) -> Int {
        let t = tokens.sorted()
        var i = 0, j = t.count - 1, score = 0, ans = 0, power = power
        while i <= j {
            if power >= t[i] {
                power -= t[i]
                i += 1
                score += 1
                ans = max(ans, score)
            } else if score > 0 {
                power += t[j]
                j -= 1
                score -= 1
            } else {
                break
            }
        }
        return ans
    }
}
