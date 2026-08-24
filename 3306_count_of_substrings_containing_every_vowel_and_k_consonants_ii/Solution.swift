// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

class Solution {
    func countOfSubstrings(_ word: String, _ k: Int) -> Int {
        return atLeast(word, k) - atLeast(word, k + 1)
    }

    private func isVowel(_ c: Character) -> Bool {
        return c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
    }

    private func atLeast(_ word: String, _ k: Int) -> Int {
        let w = Array(word)
        var cnt = [Character: Int]()
        var cons = 0, l = 0, ans = 0
        for r in 0..<w.count {
            let c = w[r]
            if isVowel(c) { cnt[c, default: 0] += 1 }
            else { cons += 1 }
            while cnt.count == 5 && cons >= k {
                ans += w.count - r
                let c2 = w[l]
                if isVowel(c2) {
                    cnt[c2, default: 0] -= 1
                    if cnt[c2] == 0 { cnt.removeValue(forKey: c2) }
                } else { cons -= 1 }
                l += 1
            }
        }
        return ans
    }
}
