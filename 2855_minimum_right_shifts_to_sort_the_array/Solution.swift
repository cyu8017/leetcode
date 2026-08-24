// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

class Solution {
    func minimumRightShifts(_ nums: [Int]) -> Int {
        let n = nums.count
        var drops = 0, idx = -1
        for i in 0..<n {
            if nums[i] > nums[(i + 1) % n] {
                drops += 1
                idx = i
            }
        }
        if drops == 0 { return 0 }
        if drops > 1 { return -1 }
        return n - 1 - idx
    }
}
