// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

class Solution {
    func getWordsInLongestSubsequence(_ words: [String], _ groups: [Int]) -> [String] {
        let n = words.count
        var dp = Array(repeating: 1, count: n)
        var prev = Array(repeating: -1, count: n)
        var best = 1, bestI = 0
        for i in 0..<n {
            for j in 0..<i {
                if groups[i] != groups[j] && hamming(words[i], words[j]) == 1 && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1
                    prev[i] = j
                }
            }
            if dp[i] > best {
                best = dp[i]
                bestI = i
            }
        }
        var path: [String] = []
        var i = bestI
        while i != -1 {
            path.append(words[i])
            i = prev[i]
        }
        return path.reversed()
    }

    private func hamming(_ a: String, _ b: String) -> Int {
        if a.count != b.count { return 100 }
        let aa = Array(a), bb = Array(b)
        var d = 0
        for i in 0..<aa.count where aa[i] != bb[i] { d += 1 }
        return d
    }
}
