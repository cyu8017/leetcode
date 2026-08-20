// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

func decodeMessage(key string, message string) string {
	mp := make([]byte, 26)
	next := byte('a')
	for i := 0; i < len(key); i++ {
		c := key[i]
		if c == ' ' || mp[c-'a'] != 0 {
			continue
		}
		mp[c-'a'] = next
		next++
	}
	out := make([]byte, len(message))
	for i := 0; i < len(message); i++ {
		if message[i] == ' ' {
			out[i] = ' '
		} else {
			out[i] = mp[message[i]-'a']
		}
	}
	return string(out)
}
