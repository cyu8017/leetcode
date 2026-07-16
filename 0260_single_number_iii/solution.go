// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

func singleNumber(nums []int) []int {
	xorAll := 0
	for _, num := range nums {
		xorAll ^= num
	}
	diff := xorAll & -xorAll
	first := 0
	second := 0
	for _, num := range nums {
		if num&diff != 0 {
			first ^= num
		} else {
			second ^= num
		}
	}
	return []int{first, second}
}
