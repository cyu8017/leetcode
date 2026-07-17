// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

func sumOfFlooredPairs(nums []int) int {
	const mod = 1_000_000_007
	maxVal := 0
	for _, num := range nums {
		if num > maxVal {
			maxVal = num
		}
	}

	count := make([]int, maxVal+1)
	for _, num := range nums {
		count[num]++
	}

	prefix := make([]int, maxVal+1)
	prefix[0] = count[0]
	for value := 1; value <= maxVal; value++ {
		prefix[value] = prefix[value-1] + count[value]
	}

	answer := 0
	for divisor := 1; divisor <= maxVal; divisor++ {
		if count[divisor] == 0 {
			continue
		}
		for quotient := 1; quotient*divisor <= maxVal; quotient++ {
			low := quotient * divisor
			high := (quotient + 1) * divisor
			if high-1 > maxVal {
				high = maxVal + 1
			}
			matches := prefix[high-1]
			if low > 0 {
				matches -= prefix[low-1]
			}
			answer = (answer + count[divisor]*matches*quotient) % mod
		}
	}

	return answer
}
