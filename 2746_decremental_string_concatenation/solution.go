// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/


func minimizeConcatenatedLength(words []string) int {
	n := len(words)
	type key struct{ i int; first, last byte }
	memo := map[key]int{}
	var dfs func(i int, first, last byte) int
	dfs = func(i int, first, last byte) int {
		if i == n {
			return 0
		}
		k := key{i, first, last}
		if v, ok := memo[k]; ok {
			return v
		}
		w := words[i]
		wf, wl := w[0], w[len(w)-1]
		// append
		add1 := len(w)
		if last == wf {
			add1--
		}
		// prepend
		add2 := len(w)
		if wl == first {
			add2--
		}
		a := add1 + dfs(i+1, first, wl)
		b := add2 + dfs(i+1, wf, last)
		best := a
		if b < best {
			best = b
		}
		memo[k] = best
		return best
	}
	w0 := words[0]
	return len(w0) + dfs(1, w0[0], w0[len(w0)-1])
}
