// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

class Solution {
    func maxDistance(_ words: [String]) -> Int {
        let n = words.count
        var ans = 0
        for i in 0..<n {
            if words[i] != words[0] { ans = max(ans, i + 1) }
            if words[i] != words[n - 1] { ans = max(ans, n - i) }
        }
        return ans
    }
}
