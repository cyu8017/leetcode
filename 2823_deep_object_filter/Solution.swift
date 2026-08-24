// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

class Solution {
    func deepFilter(_ obj: [Int], _ fn: (Int) -> Bool) -> [Int] {
        obj.filter(fn)
    }
}
