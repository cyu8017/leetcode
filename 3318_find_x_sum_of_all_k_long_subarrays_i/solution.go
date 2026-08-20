// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

func findXSum(nums []int, k int, x int) []int {
	n := len(nums)
	ans := make([]int, n-k+1)
	for i := 0; i <= n-k; i++ {
		freq := map[int]int{}
		for j := i; j < i+k; j++ {
			freq[nums[j]]++
		}
		type p struct{ v, f int }
		arr := []p{}
		for v, f := range freq {
			arr = append(arr, p{v, f})
		}
		for a := 0; a < len(arr); a++ {
			for b := a + 1; b < len(arr); b++ {
				if arr[b].f > arr[a].f || (arr[b].f == arr[a].f && arr[b].v > arr[a].v) {
					arr[a], arr[b] = arr[b], arr[a]
				}
			}
		}
		sum := 0
		lim := x
		if lim > len(arr) {
			lim = len(arr)
		}
		keep := map[int]bool{}
		for t := 0; t < lim; t++ {
			keep[arr[t].v] = true
		}
		for j := i; j < i+k; j++ {
			if keep[nums[j]] {
				sum += nums[j]
			}
		}
		ans[i] = sum
	}
	return ans
}
