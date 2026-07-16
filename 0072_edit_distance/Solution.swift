// LeetCode 0072 - Edit Distance
// https://leetcode.com/problems/edit-distance/

class Solution {
    func minDistance(_ word1: String, _ word2: String) -> Int {
        let m = word1.count
        let n = word2.count
        let w1 = Array(word1)
        let w2 = Array(word2)
        var prev = Array(0...n)
        var curr = Array(repeating: 0, count: n + 1)

        for i in 1...m {
            curr[0] = i
            for j in 1...n {
                if w1[i - 1] == w2[j - 1] {
                    curr[j] = prev[j - 1]
                } else {
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
                }
            }
            swap(&prev, &curr)
        }

        return prev[n]
    }
}
