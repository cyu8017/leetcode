// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

func countDifferentSubsequenceGCDs(nums []int) int {
	maxVal := nums[0]
	for _, num := range nums {
		if num > maxVal {
			maxVal = num
		}
	}
	present := make([]bool, maxVal+1)
	for _, num := range nums {
		present[num] = true
	}

	ans := 0
	for g := 1; g <= maxVal; g++ {
		has := false
		gcdVal := 0
		for multiple := g; multiple <= maxVal; multiple += g {
			if present[multiple] {
				has = true
				gcdVal = gcdInt(gcdVal, multiple/g)
				if gcdVal == 1 {
					break
				}
			}
		}
		if has && gcdVal == 1 {
			ans++
		}
	}
	return ans
}

func gcdInt(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
