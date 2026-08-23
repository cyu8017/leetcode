// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

public class Solution {
    public int CountTestedDevices(int[] batteryPercentages) {
        int ans = 0;
        foreach (int b in batteryPercentages) {
            if (b > ans) ans++;
        }
        return ans;
    }
}
