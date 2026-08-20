// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

func subsequencesWithMiddleMode(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	ans := 0
	// enumerate middle index
	for mid := 2; mid < n-2; mid++ {
		for a := 0; a < mid; a++ {
			for b := a + 1; b < mid; b++ {
				for c := mid + 1; c < n; c++ {
					for d := c + 1; d < n; d++ {
						seq := []int{nums[a], nums[b], nums[mid], nums[c], nums[d]}
						if uniqueMode(seq) {
							ans++
						}
					}
				}
			}
		}
	}
	return ans % mod
}

func uniqueMode(a []int) bool {
	freq := map[int]int{}
	for _, x := range a {
		freq[x]++
	}
	best, cnt := 0, 0
	for _, f := range freq {
		if f > best {
			best = f
			cnt = 1
		} else if f == best {
			cnt++
		}
	}
	return cnt == 1
}
