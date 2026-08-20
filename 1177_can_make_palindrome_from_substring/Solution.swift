// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

class Solution {
    func canMakePaliQueries(_ s: String, _ queries: [[Int]]) -> [Bool] {
        let chars = Array(s)
        var prefix = [Int](repeating: 0, count: chars.count + 1)
        var mask = 0
        for i in 0..<chars.count {
            mask ^= 1 << Int(chars[i].asciiValue! - 97)
            prefix[i + 1] = mask
        }
        return queries.map { q in
            let bits = (prefix[q[1] + 1] ^ prefix[q[0]]).nonzeroBitCount
            return bits / 2 <= q[2]
        }
    }
}
