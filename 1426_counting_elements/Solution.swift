// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

class Solution {
    func countElements(_ arr: [Int]) -> Int {
        let values = Set(arr)
        return arr.filter { values.contains($0 + 1) }.count
    }
}
