// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

class Solution {
    func mergeAlternately(_ word1: String, _ word2: String) -> String {
        let a = Array(word1)
        let b = Array(word2)
        var out = [Character]()
        var i = 0
        var j = 0
        while i < a.count || j < b.count {
            if i < a.count {
                out.append(a[i])
                i += 1
            }
            if j < b.count {
                out.append(b[j])
                j += 1
            }
        }
        return String(out)
    }
}
