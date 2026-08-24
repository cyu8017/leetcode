// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

class Solution {
    func filter(_ arr: [Int], _ fn: (Int, Int) -> Bool) -> [Int] {
        var out: [Int] = []
        for i in arr.indices where fn(arr[i], i) {
            out.append(arr[i])
        }
        return out
    }
}
