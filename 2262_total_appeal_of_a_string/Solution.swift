// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

class Solution {
    func appealSum(_ s: String) -> Int {
        var last = [Int](repeating: -1, count: 26)
        var ans = 0, cur = 0
        for (i, ch) in s.utf8.enumerated() {
            let c = Int(ch - 97)
            cur += i - last[c]
            last[c] = i
            ans += cur
        }
        return ans
    }
}
