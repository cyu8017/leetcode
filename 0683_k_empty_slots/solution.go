// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

func kEmptySlots(bulbs []int, k int) int {
	n := len(bulbs)
	days := make([]int, n)
	for day, bulb := range bulbs {
		days[bulb-1] = day + 1
	}
	ans := int(^uint(0) >> 1)
	i := 0
	for i < n-k-1 {
		left, right := i, i+k+1
		j := left + 1
		for j < right && days[j] > days[left] && days[j] > days[right] {
			j++
		}
		if j == right {
			cand := days[left]
			if days[right] > cand {
				cand = days[right]
			}
			if cand < ans {
				ans = cand
			}
			i++
		} else {
			i = j
		}
	}
	if ans == int(^uint(0)>>1) {
		return -1
	}
	return ans
}
