// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

class Solution {
    func validSequence(_ word1: String, _ word2: String) -> [Int] {
        let w1 = Array(word1), w2 = Array(word2)
        let n = w1.count, m = w2.count
        var right = Array(repeating: -1, count: m + 1)
        right[m] = n
        var j = m - 1
        var i = n - 1
        while i >= 0 && j >= 0 {
            if w1[i] == w2[j] {
                right[j] = i
                j -= 1
            }
            i -= 1
        }
        var ans = Array(repeating: 0, count: m)
        var usedSkip = false
        i = 0
        j = 0
        while j < m {
            var found = false
            while i < n {
                if w1[i] == w2[j] {
                    if canFinish(i + 1, j + 1, usedSkip, right, n, m) {
                        ans[j] = i
                        i += 1
                        found = true
                        break
                    }
                } else if !usedSkip {
                    if canFinish(i + 1, j + 1, true, right, n, m) {
                        ans[j] = i
                        i += 1
                        usedSkip = true
                        found = true
                        break
                    }
                }
                i += 1
            }
            if !found { return [] }
            j += 1
        }
        return ans
    }

    private func canFinish(_ i: Int, _ j: Int, _ usedSkip: Bool, _ right: [Int], _ n: Int, _ m: Int) -> Bool {
        if j >= m { return true }
        if !usedSkip {
            if right[j] >= i { return true }
            if j + 1 <= m && right[j + 1] > i { return true }
            if right[j] > i { return true }
            return false
        }
        return right[j] >= i
    }
}
