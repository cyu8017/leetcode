// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

func sumOfEncryptedInt(nums []int) (ans int) {
	encrypt := func(x int) int {
		mx, p := 0, 0
		for ; x > 0; x /= 10 {
			mx = max(mx, x%10)
			p = p*10 + 1
		}
		return mx * p
	}
	for _, x := range nums {
		ans += encrypt(x)
	}
	return
}
