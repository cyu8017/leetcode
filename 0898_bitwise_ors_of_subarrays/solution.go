// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

func subarrayBitwiseORs(arr []int) int {
	ans := map[int]bool{}
	cur := map[int]bool{}
	for _, x := range arr {
		nxt := map[int]bool{x: true}
		for y := range cur {
			nxt[x|y] = true
		}
		cur = nxt
		for y := range cur {
			ans[y] = true
		}
	}
	return len(ans)
}
