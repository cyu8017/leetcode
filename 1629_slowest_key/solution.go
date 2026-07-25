// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

func slowestKey(releaseTimes []int, keysPressed string) byte {
	bestDur := releaseTimes[0]
	bestKey := keysPressed[0]
	for i := 1; i < len(releaseTimes); i++ {
		dur := releaseTimes[i] - releaseTimes[i-1]
		if dur > bestDur || (dur == bestDur && keysPressed[i] > bestKey) {
			bestDur = dur
			bestKey = keysPressed[i]
		}
	}
	return bestKey
}
