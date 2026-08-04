// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

func removeDuplicates(s string, k int) string {
	type pair struct {
		ch  byte
		cnt int
	}
	stack := []pair{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if len(stack) > 0 && stack[len(stack)-1].ch == ch {
			stack[len(stack)-1].cnt++
		} else {
			stack = append(stack, pair{ch, 1})
		}
		if stack[len(stack)-1].cnt == k {
			stack = stack[:len(stack)-1]
		}
	}
	out := []byte{}
	for _, p := range stack {
		for i := 0; i < p.cnt; i++ {
			out = append(out, p.ch)
		}
	}
	return string(out)
}
