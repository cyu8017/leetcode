// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

import (
	"fmt"
	"math"
	"strconv"
)

func abbreviateProduct(left int, right int) string {
	twos, fives := 0, 0
	for i := left; i <= right; i++ {
		x := i
		for x%2 == 0 {
			twos++
			x /= 2
		}
		for x%5 == 0 {
			fives++
			x /= 5
		}
	}
	zeros := twos
	if fives < zeros {
		zeros = fives
	}
	// compute product without trailing zeros mod 1e10 for last digits, and log for first
	const MOD int64 = 100000000000 // keep extra digits
	prod := int64(1)
	extra2, extra5 := twos-zeros, fives-zeros
	logSum := 0.0
	for i := left; i <= right; i++ {
		x := i
		for x%2 == 0 {
			x /= 2
		}
		for x%5 == 0 {
			x /= 5
		}
		prod = (prod * int64(x)) % MOD
		logSum += math.Log10(float64(x))
	}
	for i := 0; i < extra2; i++ {
		prod = (prod * 2) % MOD
		logSum += math.Log10(2)
	}
	for i := 0; i < extra5; i++ {
		prod = (prod * 5) % MOD
		logSum += math.Log10(5)
	}
	// if small product, no abbreviation
	// total digits of product with zeros
	fullLog := 0.0
	for i := left; i <= right; i++ {
		fullLog += math.Log10(float64(i))
	}
	digits := int(fullLog) + 1
	if digits <= 10 {
		p := int64(1)
		for i := left; i <= right; i++ {
			p *= int64(i)
		}
		return strconv.FormatInt(p, 10)
	}
	frac := logSum - math.Floor(logSum)
	prefix := int64(math.Pow(10, frac+4)) // 5 digits
	suffix := prod % 100000
	return fmt.Sprintf("%de%d%05d", prefix, zeros, suffix)
}
