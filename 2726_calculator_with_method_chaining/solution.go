// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/


type Calculator struct{ val float64 }

func Constructor(val float64) *Calculator {
	return &Calculator{val: val}
}

func (c *Calculator) Add(v float64) *Calculator    { c.val += v; return c }
func (c *Calculator) Subtract(v float64) *Calculator { c.val -= v; return c }
func (c *Calculator) Multiply(v float64) *Calculator { c.val *= v; return c }
func (c *Calculator) Divide(v float64) *Calculator {
	if v == 0 {
		panic("Division by zero is not allowed")
	}
	c.val /= v
	return c
}
func (c *Calculator) Power(v float64) *Calculator {
	// integer-ish power via loop for simplicity when v is whole
	res := 1.0
	exp := int(v)
	base := c.val
	if v < 0 {
		exp = -exp
		for i := 0; i < exp; i++ {
			res *= base
		}
		c.val = 1 / res
		return c
	}
	for i := 0; i < exp; i++ {
		res *= base
	}
	c.val = res
	return c
}
func (c *Calculator) GetResult() float64 { return c.val }
