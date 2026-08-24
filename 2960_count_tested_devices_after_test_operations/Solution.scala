// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

object Solution {
  def countTestedDevices(batteryPercentages: Array[Int]): Int = {
    var ans = 0
    for (b <- batteryPercentages) if (b > ans) ans += 1
    ans
  }
}
