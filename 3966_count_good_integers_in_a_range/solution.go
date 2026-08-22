// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

func countGoodIntegers(l int64, r int64, k int) int64 {
	count := func(bound int64) int64 {
		if bound <= 0 {
			return 0
		}
		digits := []byte{}
		for x := bound; x > 0; x /= 10 {
			digits = append(digits, byte(x%10))
		}
		for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
			digits[i], digits[j] = digits[j], digits[i]
		}
		type state3966 struct {
			position, previous int
			started            bool
		}
		memo := make(map[state3966]int64)
		var dfs func(int, int, bool, bool) int64
		dfs = func(position, previous int, started, tight bool) int64 {
			if position == len(digits) {
				if started {
					return 1
				}
				return 0
			}
			key := state3966{position, previous, started}
			if !tight {
				if value, ok := memo[key]; ok {
					return value
				}
			}
			limit := 9
			if tight {
				limit = int(digits[position])
			}
			var result int64
			for digit := 0; digit <= limit; digit++ {
				nextStarted := started || digit != 0
				if started && abs3966(previous-digit) > k {
					continue
				}
				nextPrevious := previous
				if nextStarted {
					nextPrevious = digit
				}
				result += dfs(position+1, nextPrevious, nextStarted, tight && digit == limit)
			}
			if !tight {
				memo[key] = result
			}
			return result
		}
		return dfs(0, 0, false, true)
	}
	return count(r) - count(l-1)
}

func abs3966(x int) int {
	if x < 0 {
		return -x
	}
	return x
}