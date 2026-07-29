// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

class Solution {
    func duplicateZeros(_ arr: inout [Int]) {
        var zeros = arr.filter { $0 == 0 }.count
        let n = arr.count
        for i in stride(from: n - 1, through: 0, by: -1) {
            if i + zeros < n {
                arr[i + zeros] = arr[i]
            }
            if arr[i] == 0 {
                zeros -= 1
                if i + zeros < n {
                    arr[i + zeros] = 0
                }
            }
        }
    }
}
