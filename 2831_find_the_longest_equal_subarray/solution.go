// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

func longestEqualSubarray(nums []int, k int) int {
	pos := map[int][]int{}
	for i, v := range nums {
		pos[v] = append(pos[v], i)
	}
	ans := 0
	for _, p := range pos {
		left := 0
		for right := 0; right < len(p); right++ {
			for p[right]-p[left]-(right-left) > k {
				left++
			}
			if right-left+1 > ans {
				ans = right - left + 1
			}
		}
	}
	return ans
}
