// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

class Solution {
    func getEncryptedString(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        let n = chars.count
        return String((0..<n).map { chars[($0 + k) % n] })
    }
}
