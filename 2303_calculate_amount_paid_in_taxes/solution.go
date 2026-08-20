// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

func calculateTax(brackets [][]int, income int) float64 {
	ans := 0.0
	prev := 0
	for _, b := range brackets {
		upper, percent := b[0], b[1]
		if income <= prev {
			break
		}
		taxable := upper - prev
		if income < upper {
			taxable = income - prev
		}
		ans += float64(taxable) * float64(percent) / 100.0
		prev = upper
	}
	return ans
}
