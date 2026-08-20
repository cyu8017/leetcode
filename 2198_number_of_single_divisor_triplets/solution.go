// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

func singleDivisorTriplet(nums []int) int64 {
	freq := [101]int64{}
	for _, x := range nums {
		freq[x]++
	}
	var ans int64
	for a := 1; a <= 100; a++ {
		if freq[a] == 0 {
			continue
		}
		for b := a; b <= 100; b++ {
			if freq[b] == 0 {
				continue
			}
			for c := b; c <= 100; c++ {
				if freq[c] == 0 {
					continue
				}
				s := a + b + c
				cnt := 0
				if s%a == 0 {
					cnt++
				}
				if s%b == 0 {
					cnt++
				}
				if s%c == 0 {
					cnt++
				}
				if cnt != 1 {
					continue
				}
				if a == b && b == c {
					ans += freq[a] * (freq[a] - 1) * (freq[a] - 2)
				} else if a == b {
					ans += freq[a] * (freq[a] - 1) * freq[c] * 3
				} else if b == c {
					ans += freq[b] * (freq[b] - 1) * freq[a] * 3
				} else if a == c {
					ans += freq[a] * (freq[a] - 1) * freq[b] * 3
				} else {
					ans += freq[a] * freq[b] * freq[c] * 6
				}
			}
		}
	}
	return ans
}
