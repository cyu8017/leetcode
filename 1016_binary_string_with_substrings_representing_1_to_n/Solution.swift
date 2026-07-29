// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution {
    func queryString(_ s: String, _ n: Int) -> Bool {
        for i in stride(from: n, through: n / 2 + 1, by: -1) {
            if !s.contains(String(i, radix: 2)) { return false }
        }
        return true
    }
}
