// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

func generatePossibleNextMoves(currentState string) []string {
	result := make([]string, 0)
	state := []byte(currentState)
	for index := 0; index+1 < len(state); index++ {
		if state[index] == '+' && state[index+1] == '+' {
			nextState := append([]byte(nil), state...)
			nextState[index] = '-'
			nextState[index+1] = '-'
			result = append(result, string(nextState))
		}
	}
	return result
}
