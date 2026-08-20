// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

import (
	"math/big"
	"strings"
)

func isRationalEqual(s string, t string) bool {
	return parseRational(s).Cmp(parseRational(t)) == 0
}

func parseRational(x string) *big.Rat {
	if !strings.Contains(x, "(") {
		if x == "" {
			return big.NewRat(0, 1)
		}
		r := new(big.Rat)
		r.SetString(x)
		return r
	}
	parts := strings.Split(x, "(")
	nonRep := parts[0]
	rep := strings.TrimSuffix(parts[1], ")")
	if !strings.Contains(nonRep, ".") {
		nonRep += "."
	}
	split := strings.SplitN(nonRep, ".", 2)
	integer, frac := split[0], split[1]
	base := new(big.Rat)
	if integer == "" {
		base.SetInt64(0)
	} else {
		base.SetString(integer)
	}
	if frac != "" {
		num := new(big.Int)
		num.SetString(frac, 10)
		den := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(len(frac))), nil)
		base.Add(base, new(big.Rat).SetFrac(num, den))
	}
	if rep != "" {
		num := new(big.Int)
		num.SetString(rep, 10)
		repDen := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(len(rep))), nil)
		repDen.Sub(repDen, big.NewInt(1))
		fracDen := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(len(frac))), nil)
		den := new(big.Int).Mul(repDen, fracDen)
		base.Add(base, new(big.Rat).SetFrac(num, den))
	}
	return base
}
