// LeetCode 0189 - Rotate Array
// https://leetcode.com/problems/rotate-array/

class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        let n = nums.count
        let rotations = k % n

        func reverse(_ left: Int, _ right: Int) {
            var left = left
            var right = right
            while left < right {
                nums.swapAt(left, right)
                left += 1
                right -= 1
            }
        }

        reverse(0, n - 1)
        reverse(0, rotations - 1)
        reverse(rotations, n - 1)
    }
}