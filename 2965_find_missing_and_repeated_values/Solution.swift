// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution {
    func findMissingAndRepeatedValues(_ grid: [[Int]]) -> [Int] {
        let n = grid.count
        var freq = Array(repeating: 0, count: n * n + 1)
        for row in grid {
            for v in row { freq[v] += 1 }
        }
        var rep = 0, miss = 0
        for i in 1...(n * n) {
            if freq[i] == 2 { rep = i }
            if freq[i] == 0 { miss = i }
        }
        return [rep, miss]
    }
}
