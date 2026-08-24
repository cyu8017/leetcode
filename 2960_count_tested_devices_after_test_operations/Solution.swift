// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution {
    func countTestedDevices(_ batteryPercentages: [Int]) -> Int {
        var ans = 0
        for b in batteryPercentages where b > ans {
            ans += 1
        }
        return ans
    }
}
