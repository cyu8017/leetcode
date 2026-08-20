// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

func splitMessage(message string, limit int) []string {
	n := len(message)
	for parts := 1; parts <= n; parts++ {
		sbDigits := len(itoa(parts))
		used := 0
		ok := true
		idx := 0
		res := make([]string, 0, parts)
		for i := 1; i <= parts; i++ {
			tail := 3 + len(itoa(i)) + sbDigits // <a/b>
			cap := limit - tail
			if cap <= 0 {
				ok = false
				break
			}
			if idx >= n {
				ok = false
				break
			}
			take := cap
			if take > n-idx {
				take = n - idx
			}
			// last part must consume remaining exactly matching parts count
			res = append(res, message[idx:idx+take]+"<"+itoa(i)+"/"+itoa(parts)+">")
			idx += take
			used += take
		}
		if ok && idx == n {
			return res
		}
	}
	return []string{}
}

func itoa(x int) string {
	if x == 0 {
		return "0"
	}
	b := []byte{}
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}
