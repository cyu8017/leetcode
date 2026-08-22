// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

func maximumTotalValue(value []int, decay []int, m int64) int {
	const mod int64 = 1000000007
	countAtLeast := func(threshold int64) int64 {
		var count int64
		for i, v := range value {
			if int64(v) >= threshold {
				count += (int64(v)-threshold)/int64(decay[i]) + 1
			}
		}
		return count
	}
	if countAtLeast(1) <= m {
		var sum int64
		for i, v := range value {
			terms := (int64(v)-1)/int64(decay[i]) + 1
			sum = (sum + terms*int64(v) - int64(decay[i])*terms*(terms-1)/2) % mod
		}
		return int(sum)
	}
	high := int64(0)
	for _, v := range value {
		if int64(v) > high {
			high = int64(v)
		}
	}
	low := int64(1)
	for low < high {
		mid := (low + high + 1) / 2
		if countAtLeast(mid) >= m {
			low = mid
		} else {
			high = mid - 1
		}
	}
	threshold := low
	var count, sum int64
	for i, v := range value {
		if int64(v) < threshold {
			continue
		}
		terms := (int64(v)-threshold)/int64(decay[i]) + 1
		count += terms
		sum = (sum + (terms*int64(v)-int64(decay[i])*terms*(terms-1)/2)%mod) % mod
	}
	sum = (sum - ((count-m)%mod)*(threshold%mod)) % mod
	if sum < 0 {
		sum += mod
	}
	return int(sum)
}