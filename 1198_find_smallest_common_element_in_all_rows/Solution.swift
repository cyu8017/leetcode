// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

class Solution {
    func smallestCommonElement(_ mat: [[Int]]) -> Int {
        var count: [Int: Int] = [:]
        for row in mat {
            for x in Set(row) { count[x, default: 0] += 1 }
        }
        let n = mat.count
        return count.filter { $0.value == n }.map { $0.key }.min() ?? -1
    }
}
