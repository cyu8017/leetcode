// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
        int ans = 0;
        for (int b : batteryPercentages) {
            if (b > ans) ans++;
        }
        return ans;
    }
}
