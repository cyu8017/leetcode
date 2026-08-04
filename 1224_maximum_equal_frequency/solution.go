// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

func maxEqualFreq(nums []int) int {
	count := map[int]int{}
	frequencies := map[int]int{}
	answer := 0
	for i, x := range nums {
		old := count[x]
		if old > 0 {
			frequencies[old]--
			if frequencies[old] == 0 {
				delete(frequencies, old)
			}
		}
		count[x]++
		frequencies[old+1]++
		high := 0
		for f := range frequencies {
			if f > high {
				high = f
			}
		}
		idx := i + 1
		if high == 1 || frequencies[high]*high+1 == idx || (frequencies[high] == 1 && frequencies[high-1]*(high-1)+high == idx) {
			answer = idx
		}
	}
	return answer
}
