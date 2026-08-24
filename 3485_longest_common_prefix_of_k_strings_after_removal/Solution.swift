// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

class Solution {
    func longestCommonPrefix(_ words: [String], _ k: Int) -> [Int] {
        let n = words.count
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            var rest = [String]()
            for j in 0..<n where j != i { rest.append(words[j]) }
            if rest.count < k { ans[i] = 0; continue }
            rest.sort()
            var best = 0
            if rest.count >= k {
                for j in 0...(rest.count - k) {
                    best = max(best, lcpOf(Array(rest[j..<(j + k)])))
                }
            }
            ans[i] = best
        }
        return ans
    }

    private func lcpOf(_ a: [String]) -> Int {
        if a.isEmpty { return 0 }
        var pref = Array(a[0])
        for t in 1..<a.count {
            let s = Array(a[t])
            var i = 0
            while i < pref.count && i < s.count && pref[i] == s[i] { i += 1 }
            pref = Array(pref[..<i])
            if pref.isEmpty { return 0 }
        }
        return pref.count
    }
}
