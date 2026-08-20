// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

class Solution {
    func binarySearchableNumbers(_ nums: [Int]) -> Int {
        let n = nums.count
        var ok = Array(repeating: 1, count: n)
        var mx = Int.min, mi = Int.max
        for i in 0..<n {
            if nums[i] < mx { ok[i] = 0 } else { mx = nums[i] }
        }
        for i in stride(from: n - 1, through: 0, by: -1) {
            if nums[i] > mi { ok[i] = 0 } else { mi = nums[i] }
        }
        return ok.reduce(0, +)
    }
}
