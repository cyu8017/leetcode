// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

func countTestedDevices(batteryPercentages []int) int {
	ans := 0
	for _, b := range batteryPercentages {
		if b > ans {
			ans++
		}
	}
	return ans
}
