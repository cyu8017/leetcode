// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

class Solution {
    func kthLuckyNumber(_ k: Int) -> String {
        var k = k + 1
        var bits = ""
        while k > 1 {
            bits = (k % 2 == 0 ? "4" : "7") + bits
            k /= 2
        }
        return bits
    }
}
