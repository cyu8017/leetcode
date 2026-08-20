// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/


func beautifulSubsets(nums []int, k int) int {
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	groups := map[int][]int{}
	for x := range freq {
		groups[x%k] = append(groups[x%k], x)
	}
	ans := 1
	for _, vals := range groups {
		// sort
		for i := 0; i < len(vals); i++ {
			for j := i + 1; j < len(vals); j++ {
				if vals[j] < vals[i] {
					vals[i], vals[j] = vals[j], vals[i]
				}
			}
		}
		prevTake, prevSkip := 0, 1
		prevVal := -1 << 30
		for _, v := range vals {
			ways := 1
			for i := 0; i < freq[v]; i++ {
				ways *= 2
			}
			ways-- // non-empty of this value
			skip := prevTake + prevSkip
			take := ways * prevSkip
			if prevVal+k != v {
				take += ways * prevTake
			}
			prevTake, prevSkip = take, skip
			prevVal = v
		}
		ans *= prevTake + prevSkip
	}
	return ans - 1
}
