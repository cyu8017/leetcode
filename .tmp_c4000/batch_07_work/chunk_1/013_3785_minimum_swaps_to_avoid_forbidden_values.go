// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

func minSwaps(nums []int, forbidden []int) int {
	n := len(nums)
	freq := make(map[int]int)
	for _, x := range nums {
		freq[x]++
	}
	for _, x := range forbidden {
		freq[x]++
	}
	for _, c := range freq {
		if c > n {
			return -1
		}
	}
	bad := make(map[int]int)
	total, largest := 0, 0
	for i, x := range nums {
		if x == forbidden[i] {
			bad[x]++
			total++
			if bad[x] > largest {
				largest = bad[x]
			}
		}
	}
	if (total+1)/2 > largest {
		return (total + 1) / 2
	}
	return largest
}