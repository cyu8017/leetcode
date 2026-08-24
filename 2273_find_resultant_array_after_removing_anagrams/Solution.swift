// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution {
    func removeAnagrams(_ words: [String]) -> [String] {
        func sig(_ w: String) -> [Int] {
            var c = [Int](repeating: 0, count: 26)
            for ch in w.utf8 { c[Int(ch - 97)] += 1 }
            return c
        }
        var ans = [words[0]]
        var prev = sig(words[0])
        for i in 1..<words.count {
            let cur = sig(words[i])
            if cur != prev {
                ans.append(words[i])
                prev = cur
            }
        }
        return ans
    }
}
