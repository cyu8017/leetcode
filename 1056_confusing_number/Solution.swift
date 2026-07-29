// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

class Solution {
    func confusingNumber(_ n: Int) -> Bool {
        let rotate: [Character: Character] = [
            "0": "0", "1": "1", "6": "9", "8": "8", "9": "6"
        ]
        let s = Array(String(n))
        var rotated: [Character] = []
        for ch in s.reversed() {
            guard let r = rotate[ch] else { return false }
            rotated.append(r)
        }
        return String(rotated) != String(s)
    }
}
