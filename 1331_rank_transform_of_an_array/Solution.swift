// LeetCode 1331 - Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/

class Solution {
    func arrayRankTransform(_ arr: [Int]) -> [Int] {
        let sortedUnique = Array(Set(arr)).sorted()
        var rank = [Int: Int]()
        for (i, value) in sortedUnique.enumerated() { rank[value] = i + 1 }
        return arr.map { rank[$0]! }
    }
}
