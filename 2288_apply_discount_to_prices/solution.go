// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

import (
	"fmt"
	"strconv"
	"strings"
)

func discountPrices(sentence string, discount int) string {
	parts := strings.Fields(sentence)
	for i, p := range parts {
		if len(p) >= 2 && p[0] == '$' {
			ok := true
			for j := 1; j < len(p); j++ {
				if p[j] < '0' || p[j] > '9' {
					ok = false
					break
				}
			}
			if ok {
				val, _ := strconv.ParseInt(p[1:], 10, 64)
				price := float64(val) * (100.0 - float64(discount)) / 100.0
				parts[i] = fmt.Sprintf("$%.2f", price)
			}
		}
	}
	return strings.Join(parts, " ")
}
