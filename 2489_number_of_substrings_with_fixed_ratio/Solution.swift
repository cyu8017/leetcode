// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

class Solution {
    func fixedRatio(_ s: String, _ num1: Int, _ num2: Int) -> Int {
        var pref = [Int: Int]()
        pref[0] = 1
        var zeros = 0, ones = 0, ans = 0
        for c in s {
            if c == "0" { zeros += 1 } else { ones += 1 }
            let key = zeros * num2 - ones * num1
            ans += pref[key, default: 0]
            pref[key, default: 0] += 1
        }
        return ans
    }
}
