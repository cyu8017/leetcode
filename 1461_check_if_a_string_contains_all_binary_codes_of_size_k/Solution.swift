// LeetCode 1461 - Check If a String Contains All Binary Codes of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution {
    func hasAllCodes(_ s: String, _ k: Int) -> Bool {
        if s.count < k { return false }
        let chars = Array(s)
        var seen = Set<String>()
        for i in 0...(chars.count - k) {
            seen.insert(String(chars[i..<(i + k)]))
        }
        return seen.count == 1 << k
    }
}
