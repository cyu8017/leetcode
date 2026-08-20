// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

func twoEditWords(queries []string, dictionary []string) []string {
	ans := []string{}
	for _, q := range queries {
		ok := false
		for _, d := range dictionary {
			diff := 0
			for i := 0; i < len(q); i++ {
				if q[i] != d[i] {
					diff++
					if diff > 2 {
						break
					}
				}
			}
			if diff <= 2 {
				ok = true
				break
			}
		}
		if ok {
			ans = append(ans, q)
		}
	}
	return ans
}
