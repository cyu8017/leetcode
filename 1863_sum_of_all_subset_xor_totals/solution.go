// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

func subsetXORSum(nums []int) int {
	bits := 0
	for _, num := range nums {
		bits |= num
	}

	total := 0
	for bit := 1; bit <= bits; bit <<= 1 {
		if bits&bit != 0 {
			total += bit
		}
	}

	return total << (len(nums) - 1)
}
