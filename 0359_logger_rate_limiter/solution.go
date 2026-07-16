// LeetCode 0359 - Logger Rate Limiter
// https://leetcode.com/problems/logger-rate-limiter/

type Logger struct {
	lastPrinted map[string]int
}

func Constructor() Logger {
	return Logger{lastPrinted: make(map[string]int)}
}

func (this *Logger) ShouldPrintMessage(timestamp int, message string) bool {
	if last, ok := this.lastPrinted[message]; !ok || timestamp-last >= 10 {
		this.lastPrinted[message] = timestamp
		return true
	}
	return false
}
