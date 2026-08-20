// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

class Solution {
    func findKthPositive(_ arr: [Int], _ k: Int) -> Int {
        var left = 0, right = arr.count
        while left < right {
            let middle = (left + right) / 2
            if arr[middle] - middle - 1 < k {
                left = middle + 1
            } else {
                right = middle
            }
        }
        return left + k
    }
}
