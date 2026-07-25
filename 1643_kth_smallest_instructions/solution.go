// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

func kthSmallestPath(destination []int, k int) string {
	v, h := destination[0], destination[1]
	ans := make([]byte, 0, v+h)
	for h+v > 0 {
		if h > 0 {
			count := comb1643(h+v-1, v)
			if k <= count {
				ans = append(ans, 'H')
				h--
				continue
			}
			k -= count
		}
		ans = append(ans, 'V')
		v--
	}
	return string(ans)
}

func comb1643(n, r int) int {
	if r < 0 || r > n {
		return 0
	}
	if r > n-r {
		r = n - r
	}
	res := 1
	for i := 0; i < r; i++ {
		res = res * (n - i) / (i + 1)
	}
	return res
}
