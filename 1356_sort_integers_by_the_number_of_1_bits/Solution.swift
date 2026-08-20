// LeetCode 1356 - Sort Integers by The Number of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution {
    func sortByBits(_ arr: [Int]) -> [Int] {
        arr.sorted { a, b in
            let ca = a.nonzeroBitCount, cb = b.nonzeroBitCount
            return ca != cb ? ca < cb : a < b
        }
    }
}
