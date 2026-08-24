// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

class Solution {
    func sortBy(_ arr: [Int], _ fn: (Int) -> Double) -> [Int] {
        arr.sorted { fn($0) < fn($1) }
    }
}
