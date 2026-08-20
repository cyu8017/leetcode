// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

class Solution {
    func missingNumber(_ arr: [Int]) -> Int {
        let n = arr.count
        let diff = (arr[n - 1] - arr[0]) / n
        for i in 1..<n {
            if arr[i] != arr[i - 1] + diff {
                return arr[i - 1] + diff
            }
        }
        return arr[0]
    }
}
