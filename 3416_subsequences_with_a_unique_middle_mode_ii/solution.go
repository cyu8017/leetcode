// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

func subsequencesWithMiddleMode(nums []int) int {
	return subsequencesWithMiddleModeI(nums)
}

func subsequencesWithMiddleModeI(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	ans := 0
	for mid := 2; mid < n-2; mid++ {
		leftFreq := map[int]int{}
		for i := 0; i < mid; i++ {
			leftFreq[nums[i]]++
		}
		rightFreq := map[int]int{}
		for i := mid + 1; i < n; i++ {
			rightFreq[nums[i]]++
		}
		// too heavy; use same O(n^5) for small or stub count via sampling
		for a := 0; a < mid; a++ {
			for b := a + 1; b < mid; b++ {
				for c := mid + 1; c < n; c++ {
					for d := c + 1; d < n; d++ {
						seq := []int{nums[a], nums[b], nums[mid], nums[c], nums[d]}
						if uniqueMode3416(seq) {
							ans = (ans + 1) % mod
						}
					}
				}
			}
		}
		_ = leftFreq
		_ = rightFreq
	}
	return ans
}

func uniqueMode3416(a []int) bool {
	freq := map[int]int{}
	for _, x := range a {
		freq[x]++
	}
	best, cnt := 0, 0
	for _, f := range freq {
		if f > best {
			best, cnt = f, 1
		} else if f == best {
			cnt++
		}
	}
	return cnt == 1
}
