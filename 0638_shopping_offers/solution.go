// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

func shoppingOffers(price []int, special [][]int, needs []int) int {
	n := len(price)
	memo := map[string]int{}
	encode := func(state []int) string {
		b := make([]byte, 0, len(state)*2)
		for _, v := range state {
			b = append(b, byte(v)+'0', ',')
		}
		return string(b)
	}
	var dfs func(state []int) int
	dfs = func(state []int) int {
		key := encode(state)
		if v, ok := memo[key]; ok {
			return v
		}
		cost := 0
		for i := 0; i < n; i++ {
			cost += state[i] * price[i]
		}
		for _, offer := range special {
			nxt := append([]int(nil), state...)
			valid := true
			for i := 0; i < n; i++ {
				if nxt[i] < offer[i] {
					valid = false
					break
				}
				nxt[i] -= offer[i]
			}
			if valid {
				cand := offer[n] + dfs(nxt)
				if cand < cost {
					cost = cand
				}
			}
		}
		memo[key] = cost
		return cost
	}
	return dfs(needs)
}
