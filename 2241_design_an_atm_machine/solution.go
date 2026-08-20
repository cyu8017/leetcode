// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

type ATM struct {
	cnt  [5]int64
	vals [5]int
}

func Constructor() ATM {
	return ATM{vals: [5]int{20, 50, 100, 200, 500}}
}

func (this *ATM) Deposit(banknotesCount []int) {
	for i := 0; i < 5; i++ {
		this.cnt[i] += int64(banknotesCount[i])
	}
}

func (this *ATM) Withdraw(amount int) []int {
	take := make([]int, 5)
	remain := int64(amount)
	tmp := this.cnt
	for i := 4; i >= 0; i-- {
		need := remain / int64(this.vals[i])
		if need > tmp[i] {
			need = tmp[i]
		}
		take[i] = int(need)
		remain -= need * int64(this.vals[i])
	}
	if remain != 0 {
		return []int{-1}
	}
	for i := 0; i < 5; i++ {
		this.cnt[i] -= int64(take[i])
	}
	return take
}
