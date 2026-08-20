// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

func largestWordCount(messages []string, senders []string) string {
	count := map[string]int{}
	best := ""
	bestCnt := -1
	for i, msg := range messages {
		words := 1
		for j := 0; j < len(msg); j++ {
			if msg[j] == ' ' {
				words++
			}
		}
		count[senders[i]] += words
		c := count[senders[i]]
		if c > bestCnt || (c == bestCnt && senders[i] > best) {
			bestCnt = c
			best = senders[i]
		}
	}
	return best
}
