// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

func primeSubarray(nums []int, k int) int {
	mx := 0
	for _, v := range nums {
		if v > mx {
			mx = v
		}
	}
	isPrime := make([]bool, mx+1)
	for i := 2; i <= mx; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= mx; i++ {
		if isPrime[i] {
			for j := i * i; j <= mx; j += i {
				isPrime[j] = false
			}
		}
	}
	n := len(nums)
	ans := 0
	// sliding window: subarrays where primes' max-min <= k and at least 2 primes
	for l := 0; l < n; l++ {
		primes := []int{}
		for r := l; r < n; r++ {
			if isPrime[nums[r]] {
				primes = append(primes, nums[r])
			}
			if len(primes) >= 2 {
				mn, mxp := primes[0], primes[0]
				for _, p := range primes {
					if p < mn {
						mn = p
					}
					if p > mxp {
						mxp = p
					}
				}
				if mxp-mn <= k {
					ans++
				}
			}
		}
	}
	return ans
}
