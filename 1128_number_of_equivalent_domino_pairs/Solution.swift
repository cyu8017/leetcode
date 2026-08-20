// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution {
    func numEquivDominoPairs(_ dominoes: [[Int]]) -> Int {
        var count: [Int: Int] = [:]
        var ans = 0
        for d in dominoes {
            let a = min(d[0], d[1]), b = max(d[0], d[1])
            let key = a * 10 + b
            ans += count[key, default: 0]
            count[key, default: 0] += 1
        }
        return ans
    }
}
