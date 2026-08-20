// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

func countExcellentPairs(nums []int, k int) int64 {
	uniq := map[int]bool{}
	for _, x := range nums {
		uniq[x] = true
	}
	cnt := make([]int, 32)
	for x := range uniq {
		bits := 0
		for y := x; y > 0; y >>= 1 {
			bits += y & 1
		}
		cnt[bits]++
	}
	var ans int64
	for i := 0; i < 32; i++ {
		for j := 0; j < 32; j++ {
			if i+j >= k {
				ans += int64(cnt[i]) * int64(cnt[j])
			}
		}
	}
	return ans
}
