// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

func findShortestSubArray(nums []int) int {
	first := map[int]int{}
	last := map[int]int{}
	count := map[int]int{}
	for i, num := range nums {
		if _, ok := first[num]; !ok {
			first[num] = i
		}
		last[num] = i
		count[num]++
	}
	degree := 0
	for _, freq := range count {
		if freq > degree {
			degree = freq
		}
	}
	best := len(nums)
	for num, freq := range count {
		if freq == degree {
			length := last[num] - first[num] + 1
			if length < best {
				best = length
			}
		}
	}
	return best
}
