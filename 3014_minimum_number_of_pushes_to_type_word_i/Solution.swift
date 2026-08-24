// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution {
    func minimumPushes(_ word: String) -> Int {
        let n = word.count
        var ans = 0, k = 1
        for _ in 0..<(n / 8) {
            ans += k * 8
            k += 1
        }
        ans += k * (n % 8)
        return ans
    }
}
