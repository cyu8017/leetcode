// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

class Solution {
    func isStrobogrammatic(_ num: String) -> Bool {
        let mapping: [Character: Character] = ["0": "0", "1": "1", "6": "9", "8": "8", "9": "6"]
        let chars = Array(num)
        var left = 0
        var right = chars.count - 1
        while left <= right {
            if mapping[chars[left]] != chars[right] {
                return false
            }
            left += 1
            right -= 1
        }
        return true
    }
}
