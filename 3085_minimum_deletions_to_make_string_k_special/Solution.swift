// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

class Solution {
    func minimumDeletions(_ word: String, _ k: Int) -> Int {
        var freq = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        for ch in word {
            freq[Int(ch.asciiValue! - a)] += 1
        }
        let nums = freq.filter { $0 > 0 }
        var ans = word.count
        for i in 0...word.count {
            var cur = 0
            for x in nums {
                if x < i { cur += x }
                else if x > i + k { cur += x - i - k }
            }
            ans = min(ans, cur)
        }
        return ans
    }
}
