// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

int countTestedDevices(int* batteryPercentages, int batteryPercentagesSize) {
    int ans = 0;
    for (int i = 0; i < batteryPercentagesSize; i++) {
        if (batteryPercentages[i] > ans) {
            ans++;
        }
    }
    return ans;
}
