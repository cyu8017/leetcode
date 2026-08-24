// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

class Solution {
    func minimumSwaps(_ nums: [Int]) -> Int {
        let n = nums.count
        var minI = 0, maxI = 0
        for i in 1..<n {
            if nums[i] < nums[minI] { minI = i }
            if nums[i] >= nums[maxI] { maxI = i }
        }
        var ans = minI + (n - 1 - maxI)
        if minI > maxI { ans -= 1 }
        return ans
    }
}
