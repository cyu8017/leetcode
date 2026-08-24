// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution {
    func maxFreqSum(_ s: String) -> Int {
        var cnt = Array(repeating: 0, count: 26)
        for c in s.utf8 { cnt[Int(c - 97)] += 1 }
        var a = 0, b = 0
        for i in 0..<26 {
            if i == 0 || i == 4 || i == 8 || i == 14 || i == 20 {
                a = max(a, cnt[i])
            } else {
                b = max(b, cnt[i])
            }
        }
        return a + b
    }
}
