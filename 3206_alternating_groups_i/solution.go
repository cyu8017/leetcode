// LeetCode 3206 - Alternating Groups I
// https://leetcode.com/problems/alternating-groups-i/

func numberOfAlternatingGroups(colors []int) (ans int) {
	k := 3
	n := len(colors)
	cnt := 0
	for i := 0; i < n<<1; i++ {
		if i > 0 && colors[i%n] == colors[(i-1)%n] {
			cnt = 1
		} else {
			cnt++
		}
		if i >= n && cnt >= k {
			ans++
		}
	}
	return
}
