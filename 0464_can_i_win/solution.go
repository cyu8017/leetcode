// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

func canIWin(maxChoosableInteger int, desiredTotal int) bool {
	if desiredTotal <= 0 {
		return true
	}
	total := maxChoosableInteger * (maxChoosableInteger + 1) / 2
	if total < desiredTotal {
		return false
	}

	memo := make(map[int]bool)

	var canWin func(state int, currentTotal int) bool
	canWin = func(state int, currentTotal int) bool {
		if result, ok := memo[state]; ok {
			return result
		}
		for pick := 1; pick <= maxChoosableInteger; pick++ {
			bit := 1 << (pick - 1)
			if state&bit != 0 {
				continue
			}
			if currentTotal+pick >= desiredTotal {
				memo[state] = true
				return true
			}
			if !canWin(state|bit, currentTotal+pick) {
				memo[state] = true
				return true
			}
		}
		memo[state] = false
		return false
	}

	return canWin(0, 0)
}
