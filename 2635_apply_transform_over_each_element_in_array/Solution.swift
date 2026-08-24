// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

class Solution {
    func map(_ arr: [Int], _ fn: (Int, Int) -> Int) -> [Int] {
        var out = Array(repeating: 0, count: arr.count)
        for i in arr.indices { out[i] = fn(arr[i], i) }
        return out
    }
}
