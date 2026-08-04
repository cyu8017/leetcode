// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

import "strconv"
import "strings"

func invalidTransactions(transactions []string) []string {
	type tx struct {
		name, city, raw string
		time, amount    int
	}
	parsed := make([]tx, len(transactions))
	for i, t := range transactions {
		parts := strings.Split(t, ",")
		tm, _ := strconv.Atoi(parts[1])
		am, _ := strconv.Atoi(parts[2])
		parsed[i] = tx{parts[0], parts[3], t, tm, am}
	}
	invalid := map[string]bool{}
	for i := 0; i < len(parsed); i++ {
		a := parsed[i]
		if a.amount > 1000 {
			invalid[a.raw] = true
		}
		for j := 0; j < len(parsed); j++ {
			if i == j {
				continue
			}
			b := parsed[j]
			diff := a.time - b.time
			if diff < 0 {
				diff = -diff
			}
			if a.name == b.name && a.city != b.city && diff <= 60 {
				invalid[a.raw] = true
				invalid[b.raw] = true
			}
		}
	}
	ans := []string{}
	for _, t := range transactions {
		if invalid[t] {
			ans = append(ans, t)
		}
	}
	return ans
}
