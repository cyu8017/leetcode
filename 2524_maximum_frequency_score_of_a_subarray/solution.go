// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

const MOD2524 = 1000000007

func modPow2524(a, e int64) int64 {
	res := int64(1)
	a %= MOD2524
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD2524
		}
		a = a * a % MOD2524
		e >>= 1
	}
	return res
}

func maxFrequencyScore(nums []int, k int) int {
	freq := map[int]int{}
	score := int64(0)
	add := func(x int) {
		c := freq[x]
		if c > 0 {
			score = (score - modPow2524(int64(x), int64(c)) + MOD2524) % MOD2524
		}
		freq[x] = c + 1
		score = (score + modPow2524(int64(x), int64(c+1))) % MOD2524
	}
	remove := func(x int) {
		c := freq[x]
		score = (score - modPow2524(int64(x), int64(c)) + MOD2524) % MOD2524
		if c == 1 {
			delete(freq, x)
		} else {
			freq[x] = c - 1
			score = (score + modPow2524(int64(x), int64(c-1))) % MOD2524
		}
	}
	best := int64(0)
	for i := 0; i < len(nums); i++ {
		add(nums[i])
		if i >= k {
			remove(nums[i-k])
		}
		if i >= k-1 && score > best {
			best = score
		}
	}
	return int(best)
}
