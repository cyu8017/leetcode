// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

var countTestedDevices = function(batteryPercentages) {
    let ans = 0;
    for (const b of batteryPercentages) {
        if (b > ans) ans++;
    }
    return ans;
};
