// LeetCode 1352 - Product of the Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

type ProductOfNumbers struct {
	p []int
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{p: []int{1}}
}

func (this *ProductOfNumbers) Add(num int) {
	if num == 0 {
		this.p = []int{1}
	} else {
		this.p = append(this.p, this.p[len(this.p)-1]*num)
	}
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	if k >= len(this.p) {
		return 0
	}
	return this.p[len(this.p)-1] / this.p[len(this.p)-1-k]
}
