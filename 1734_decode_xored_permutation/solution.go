// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

func decode(encoded []int) []int {
	n := len(encoded) + 1
	total := 0
	for value := 1; value <= n; value++ {
		total ^= value
	}
	odd := 0
	for i := 1; i < len(encoded); i += 2 {
		odd ^= encoded[i]
	}
	ans := make([]int, n)
	ans[0] = total ^ odd
	for i, value := range encoded {
		ans[i+1] = ans[i] ^ value
	}
	return ans
}
