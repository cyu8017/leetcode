// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

import (
	"math/big"
)

func smallestGoodBase(n string) string {
	num, _ := new(big.Int).SetString(n, 10)
	maxLength := num.BitLen()
	one := big.NewInt(1)
	two := big.NewInt(2)
	for length := maxLength; length >= 2; length-- {
		low := new(big.Int).Set(two)
		high := new(big.Int).Sub(num, one)
		for low.Cmp(high) <= 0 {
			mid := new(big.Int).Add(low, new(big.Int).Rsh(new(big.Int).Sub(high, low), 1))
			total := new(big.Int).Set(one)
			power := new(big.Int).Set(one)
			ok := true
			for i := 1; i < length; i++ {
				power.Mul(power, mid)
				total.Add(total, power)
				if total.Cmp(num) > 0 {
					ok = false
					break
				}
			}
			if ok && total.Cmp(num) == 0 {
				return mid.String()
			}
			if !ok || total.Cmp(num) > 0 {
				high.Sub(mid, one)
			} else {
				low.Add(mid, one)
			}
		}
	}
	return new(big.Int).Sub(num, one).String()
}
