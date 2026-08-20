// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

class Solution {
    func encode(_ num: Int) -> String {
        String(num + 1, radix: 2).dropFirst().description
    }
}
