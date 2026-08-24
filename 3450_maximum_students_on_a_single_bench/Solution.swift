// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

class Solution {
    func maxStudentsOnBench(_ students: [[Int]]) -> Int {
        var bench = [Int: Set<Int>]()
        for s in students { bench[s[1], default: []].insert(s[0]) }
        return bench.values.map { $0.count }.max() ?? 0
    }
}
