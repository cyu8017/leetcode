// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution {
    func minimumDeletions(_ nums: [Int]) -> Int {
        let n = nums.count
        var mi = 0, ma = 0
        for i in 0..<n {
            if nums[i] < nums[mi] { mi = i }
            if nums[i] > nums[ma] { ma = i }
        }
        if mi > ma { swap(&mi, &ma) }
        return min(ma + 1, min(n - mi, mi + 1 + n - ma))
    }
}
