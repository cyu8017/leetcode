// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution {
    fun countTestedDevices(batteryPercentages: IntArray): Int {
        var ans = 0
        for (b in batteryPercentages) {
            if (b > ans) ans++
        }
        return ans
    }
}
