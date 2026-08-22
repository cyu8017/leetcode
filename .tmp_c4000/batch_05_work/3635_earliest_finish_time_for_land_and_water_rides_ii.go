// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	x := calc(landStartTime, landDuration, waterStartTime, waterDuration)
	y := calc(waterStartTime, waterDuration, landStartTime, landDuration)
	return min(x, y)
}

func calc(a1 []int, t1 []int, a2 []int, t2 []int) int {
	minEnd := math.MaxInt32
	for i := 0; i < len(a1); i++ {
		minEnd = min(minEnd, a1[i]+t1[i])
	}
	ans := math.MaxInt32
	for i := 0; i < len(a2); i++ {
		ans = min(ans, max(minEnd, a2[i])+t2[i])
	}
	return ans
}
