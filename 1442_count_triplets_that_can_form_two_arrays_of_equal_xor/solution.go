// LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

func countTriplets(arr []int) int {
	answer := 0
	for i := range arr {
		value := 0
		for k := i; k < len(arr); k++ {
			value ^= arr[k]
			if value == 0 {
				answer += k - i
			}
		}
	}
	return answer
}
