// LeetCode 1357 - Apply Discount Every n Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

type Cashier struct {
	n, discount, count int
	prices             map[int]int
}

func Constructor(n int, discount int, products []int, prices []int) Cashier {
	m := map[int]int{}
	for i, p := range products {
		m[p] = prices[i]
	}
	return Cashier{n: n, discount: discount, prices: m}
}

func (this *Cashier) GetBill(product []int, amount []int) float64 {
	this.count++
	total := 0.0
	for i, p := range product {
		total += float64(this.prices[p] * amount[i])
	}
	if this.count%this.n == 0 {
		total = total * float64(100-this.discount) / 100.0
	}
	return total
}
