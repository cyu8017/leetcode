// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

func minOperations(nums []int, target int) int {
	cnt := make([]int, 32)
	sum := int64(0)
	for _, v := range nums {
		sum += int64(v)
		b := 0
		for 1<<b < v {
			b++
		}
		cnt[b]++
	}
	if sum < int64(target) {
		return -1
	}
	ans := 0
	for i := 0; i < 31; i++ {
		if target&(1<<i) != 0 {
			if cnt[i] > 0 {
				cnt[i]--
			} else {
				j := i + 1
				for j < 32 && cnt[j] == 0 {
					j++
				}
				if j == 32 {
					return -1
				}
				for j > i {
					cnt[j]--
					cnt[j-1] += 2
					ans++
					j--
				}
				cnt[i]--
			}
		}
		cnt[i+1] += cnt[i] / 2
	}
	return ans
}
