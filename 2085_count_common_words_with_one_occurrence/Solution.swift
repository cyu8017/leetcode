// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution {
    func countWords(_ words1: [String], _ words2: [String]) -> Int {
        var f1 = [String: Int](), f2 = [String: Int]()
        for w in words1 { f1[w, default: 0] += 1 }
        for w in words2 { f2[w, default: 0] += 1 }
        return f1.filter { $0.value == 1 && f2[$0.key, default: 0] == 1 }.count
    }
}
