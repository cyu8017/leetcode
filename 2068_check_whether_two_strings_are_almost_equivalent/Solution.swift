// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution {
    func checkAlmostEquivalent(_ word1: String, _ word2: String) -> Bool {
        var freq = [Int](repeating: 0, count: 26)
        let a = Array(word1), b = Array(word2)
        for i in 0..<a.count {
            freq[Int(a[i].asciiValue! - 97)] += 1
            freq[Int(b[i].asciiValue! - 97)] -= 1
        }
        return freq.allSatisfy { $0 >= -3 && $0 <= 3 }
    }
}
