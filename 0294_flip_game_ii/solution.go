// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

func canWin(currentState string) bool {
	memo := make(map[string]bool)

	var canWinState func(state string) bool
	canWinState = func(state string) bool {
		if value, ok := memo[state]; ok {
			return value
		}

		bytes := []byte(state)
		for index := 0; index+1 < len(bytes); index++ {
			if bytes[index] == '+' && bytes[index+1] == '+' {
				nextState := append([]byte(nil), bytes...)
				nextState[index] = '-'
				nextState[index+1] = '-'
				if !canWinState(string(nextState)) {
					memo[state] = true
					return true
				}
			}
		}

		memo[state] = false
		return false
	}

	return canWinState(currentState)
}
