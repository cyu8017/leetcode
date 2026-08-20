// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

import (
	"sort"
	"strconv"
)

func minimumCost(nums []int) int64 {
	sort.Ints(nums)
	n := len(nums)
	median := nums[n/2]
	makePal := func(x int) int {
		s := strconv.Itoa(x)
		b := []byte(s)
		for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
			b[j] = b[i]
		}
		v, _ := strconv.Atoi(string(b))
		return v
	}
	candidates := []int{}
	base := makePal(median)
	candidates = append(candidates, base)
	// nearby palindromes
	s := strconv.Itoa(median)
	half, _ := strconv.Atoi(s[:(len(s)+1)/2])
	for d := -2; d <= 2; d++ {
		h := half + d
		if h <= 0 {
			continue
		}
		hs := strconv.Itoa(h)
		var pal string
		if len(s)%2 == 0 {
			rb := []byte(hs)
			for i, j := 0, len(rb)-1; i < j; i, j = i+1, j-1 {
				rb[i], rb[j] = rb[j], rb[i]
			}
			pal = hs + string(rb)
		} else {
			rb := []byte(hs[:len(hs)-1])
			for i, j := 0, len(rb)-1; i < j; i, j = i+1, j-1 {
				rb[i], rb[j] = rb[j], rb[i]
			}
			pal = hs + string(rb)
		}
		v, err := strconv.Atoi(pal)
		if err == nil {
			candidates = append(candidates, v)
		}
	}
	candidates = append(candidates, 1, 9, 11, 99, 101)
	cost := func(p int) int64 {
		var c int64
		for _, v := range nums {
			d := v - p
			if d < 0 {
				d = -d
			}
			c += int64(d)
		}
		return c
	}
	var ans int64 = 1 << 62
	for _, p := range candidates {
		if p <= 0 {
			continue
		}
		c := cost(p)
		if c < ans {
			ans = c
		}
	}
	return ans
}
