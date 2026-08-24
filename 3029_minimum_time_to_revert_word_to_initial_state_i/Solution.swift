// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

class Solution {
    func minimumTimeToInitialState(_ word: String, _ k: Int) -> Int {
        let n = word.count
        let chars = Array(word)
        var i = k
        while i < n {
            if Array(chars[i...]) == Array(chars[0..<(n - i)]) { return i / k }
            i += k
        }
        return (n + k - 1) / k
    }
}
