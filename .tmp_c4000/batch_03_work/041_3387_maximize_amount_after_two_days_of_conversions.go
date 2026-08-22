// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

func maxAmount(initialCurrency string, pairs1 [][]string, rates1 []float64, pairs2 [][]string, rates2 []float64) float64 {
	day1 := bellman(initialCurrency, pairs1, rates1)
	day2 := bellman(initialCurrency, pairs2, rates2)
	// After day1 we have amounts in various currencies, then convert on day2 back
	// Build reverse graph for day2 from each currency amount
	ans := 1.0
	currencies := map[string]bool{initialCurrency: true}
	for _, p := range pairs1 {
		currencies[p[0]] = true
		currencies[p[1]] = true
	}
	for _, p := range pairs2 {
		currencies[p[0]] = true
		currencies[p[1]] = true
	}
	// amounts after day1
	amt1 := day1
	// from each currency c with amt1[c], run day2 conversions starting with that amount
	g2 := buildRateGraph(pairs2, rates2)
	for c, a := range amt1 {
		if a <= 0 {
			continue
		}
		dist := map[string]float64{c: a}
		updated := true
		nodes := []string{}
		for x := range currencies {
			nodes = append(nodes, x)
		}
		for it := 0; it < len(nodes) && updated; it++ {
			updated = false
			for from, edges := range g2 {
				if dist[from] == 0 {
					continue
				}
				for to, rate := range edges {
					nv := dist[from] * rate
					if nv > dist[to] {
						dist[to] = nv
						updated = true
					}
				}
			}
		}
		if dist[initialCurrency] > ans {
			ans = dist[initialCurrency]
		}
	}
	_ = day2
	return ans
}

func bellman(start string, pairs [][]string, rates []float64) map[string]float64 {
	g := buildRateGraph(pairs, rates)
	dist := map[string]float64{start: 1.0}
	for it := 0; it < 100; it++ {
		updated := false
		for from, edges := range g {
			if dist[from] == 0 {
				continue
			}
			for to, rate := range edges {
				nv := dist[from] * rate
				if nv > dist[to] {
					dist[to] = nv
					updated = true
				}
			}
		}
		if !updated {
			break
		}
	}
	return dist
}

func buildRateGraph(pairs [][]string, rates []float64) map[string]map[string]float64 {
	g := map[string]map[string]float64{}
	for i, p := range pairs {
		a, b := p[0], p[1]
		if g[a] == nil {
			g[a] = map[string]float64{}
		}
		if g[b] == nil {
			g[b] = map[string]float64{}
		}
		g[a][b] = rates[i]
		g[b][a] = 1.0 / rates[i]
	}
	return g
}
