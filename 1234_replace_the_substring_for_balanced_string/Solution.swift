// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution {
    func balancedString(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count, need = n / 4
        var count: [Character: Int] = [:]
        for ch in chars { count[ch, default: 0] += 1 }
        if count.values.allSatisfy({ $0 <= need }) { return 0 }
        var ans = n, left = 0
        for right in 0..<n {
            count[chars[right], default: 0] -= 1
            while count.values.allSatisfy({ $0 <= need }) {
                ans = min(ans, right - left + 1)
                count[chars[left], default: 0] += 1
                left += 1
            }
        }
        return ans
    }
}
