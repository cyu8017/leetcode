// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

func captureForts(forts []int) int {
	ans := 0
	prev := -1
	for i, v := range forts {
		if v != 0 {
			if prev >= 0 && forts[prev] == -v {
				if i-prev-1 > ans {
					ans = i - prev - 1
				}
			}
			prev = i
		}
	}
	return ans
}
