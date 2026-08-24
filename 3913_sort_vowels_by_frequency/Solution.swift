// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

class Solution {
    func sortVowels(_ s: String) -> String {
        let vowelsSet: Set<Character> = ["a", "e", "i", "o", "u"]
        var vowels = [Character]()
        var cnt = [Character: Int]()
        for c in s {
            if !vowelsSet.contains(c) { continue }
            if cnt[c] == nil { vowels.append(c) }
            cnt[c, default: 0] += 1
        }
        vowels.sort { cnt[$0]! > cnt[$1]! }
        var ans = Array(s)
        var i = 0
        for k in 0..<ans.count {
            if !vowelsSet.contains(ans[k]) { continue }
            let ch = vowels[i]
            ans[k] = ch
            cnt[ch]! -= 1
            if cnt[ch] == 0 { i += 1 }
        }
        return String(ans)
    }
}
