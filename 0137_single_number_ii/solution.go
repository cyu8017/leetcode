// LeetCode 0137 - Single Number II
func singleNumber(nums []int) int {
	ones, twos := 0, 0
	for _, value := range nums { ones = (ones ^ value) &^ twos; twos = (twos ^ value) &^ ones }
	return ones
}