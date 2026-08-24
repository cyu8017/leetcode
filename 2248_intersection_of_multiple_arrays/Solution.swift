// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution {
    func intersection(_ nums: [[Int]]) -> [Int] {
        var freq: [Int: Int] = [:]
        for arr in nums {
            for x in Set(arr) { freq[x, default: 0] += 1 }
        }
        return freq.filter { $0.value == nums.count }.map { $0.key }.sorted()
    }
}
