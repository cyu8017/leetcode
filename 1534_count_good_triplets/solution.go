// LeetCode 1534 - Count Good Triplets
// https://leetcode.com/problems/count-good-triplets/

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func countGoodTriplets(arr []int, a int, b int, c int) int {
	ans := 0
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if abs(arr[i]-arr[j]) > a {
				continue
			}
			for k := j + 1; k < n; k++ {
				if abs(arr[j]-arr[k]) <= b && abs(arr[i]-arr[k]) <= c {
					ans++
				}
			}
		}
	}
	return ans
}
