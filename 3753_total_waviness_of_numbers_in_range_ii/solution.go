// LeetCode 3753 - Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

type wavinessResult3753 struct {
	count int64
	sum   int64
}

func totalWaviness(a int64, b int64) int64 {
	return wavinessUpTo3753(b) - wavinessUpTo3753(a-1)
}

func wavinessUpTo3753(limit int64) int64 {
	if limit < 0 {
		return 0
	}
	digits := make([]int, 0, 16)
	if limit == 0 {
		digits = append(digits, 0)
	} else {
		for value := limit; value > 0; value /= 10 {
			digits = append(digits, int(value%10))
		}
		for left, right := 0, len(digits)-1; left < right; left, right = left+1, right-1 {
			digits[left], digits[right] = digits[right], digits[left]
		}
	}

	type state struct {
		position   int
		secondLast int
		last       int
		started    bool
	}
	memo := make(map[state]wavinessResult3753)
	var dfs func(int, int, int, bool, bool) wavinessResult3753
	dfs = func(position, secondLast, last int, started, tight bool) wavinessResult3753 {
		if position == len(digits) {
			return wavinessResult3753{count: 1}
		}
		key := state{position, secondLast, last, started}
		if !tight {
			if result, exists := memo[key]; exists {
				return result
			}
		}
		upper := 9
		if tight {
			upper = digits[position]
		}
		result := wavinessResult3753{}
		for digit := 0; digit <= upper; digit++ {
			nextTight := tight && digit == upper
			nextSecondLast, nextLast := secondLast, last
			nextStarted := started || digit != 0
			add := int64(0)
			if !nextStarted {
				nextSecondLast, nextLast = 10, 10
			} else if !started {
				nextSecondLast, nextLast = 10, digit
			} else {
				if secondLast != 10 &&
					(last > secondLast && last > digit || last < secondLast && last < digit) {
					add = 1
				}
				nextSecondLast, nextLast = last, digit
			}
			child := dfs(position+1, nextSecondLast, nextLast, nextStarted, nextTight)
			result.count += child.count
			result.sum += child.sum + add*child.count
		}
		if !tight {
			memo[key] = result
		}
		return result
	}
	return dfs(0, 10, 10, false, true).sum
}