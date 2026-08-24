// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution {
    func countHillValley(_ nums: [Int]) -> Int {
        var compact: [Int] = [nums[0]]
        for x in nums.dropFirst() where x != compact.last! {
            compact.append(x)
        }
        var ans = 0
        if compact.count >= 3 {
            for i in 1..<(compact.count - 1) {
                if (compact[i] > compact[i - 1] && compact[i] > compact[i + 1])
                    || (compact[i] < compact[i - 1] && compact[i] < compact[i + 1]) {
                    ans += 1
                }
            }
        }
        return ans
    }
}
