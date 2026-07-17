// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution {
    func largestMerge(_ word1: String, _ word2: String) -> String {
        let a = Array(word1)
        let b = Array(word2)

        func suffixGreater(_ i: Int, _ j: Int) -> Bool {
            var x = i
            var y = j
            while x < a.count && y < b.count {
                if a[x] != b[y] {
                    return a[x] > b[y]
                }
                x += 1
                y += 1
            }
            return x < a.count
        }

        var i = 0
        var j = 0
        var out = [Character]()
        while i < a.count && j < b.count {
            if suffixGreater(i, j) {
                out.append(a[i])
                i += 1
            } else {
                out.append(b[j])
                j += 1
            }
        }
        out.append(contentsOf: a[i...])
        out.append(contentsOf: b[j...])
        return String(out)
    }
}
