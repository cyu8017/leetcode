// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

func duplicateNumbersXOR(nums []int) (ans int) {
	cnt := [51]int{}
	for _, x := range nums {
		cnt[x]++
		if cnt[x] == 2 {
			ans ^= x
		}
	}
	return
}
