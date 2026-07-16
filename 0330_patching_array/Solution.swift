// LeetCode 0330 - Patching Array
// https://leetcode.com/problems/patching-array/

class Solution {
    func minPatches(_ nums: [Int], _ n: Int) -> Int {
        var patches = 0
        var miss = 1
        var index = 0
        while miss <= n {
            if index < nums.count && nums[index] <= miss {
                miss += nums[index]
                index += 1
            } else {
                miss += miss
                patches += 1
            }
        }
        return patches
    }
}
