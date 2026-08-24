// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution {
    func minimumPushes(_ word: String) -> Int {
        var cnt = Array(repeating: 0, count: 26)
        let aVal = Int(Character("a").asciiValue!)
        for ch in word { cnt[Int(ch.asciiValue!) - aVal] += 1 }
        cnt.sort()
        var ans = 0
        for i in 0..<26 {
            ans += (i / 8 + 1) * cnt[26 - i - 1]
        }
        return ans
    }
}
