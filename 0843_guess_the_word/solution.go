// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

type Master interface {
	Guess(word string) int
}

func findSecretWord(words []string, master Master) {
	match := func(a, b string) int {
		cnt := 0
		for i := 0; i < len(a); i++ {
			if a[i] == b[i] {
				cnt++
			}
		}
		return cnt
	}
	candidates := append([]string{}, words...)
	for len(candidates) > 0 {
		best := candidates[0]
		bestScore := int(^uint(0) >> 1)
		for _, w := range candidates {
			buckets := make([]int, 7)
			for _, c := range candidates {
				buckets[match(w, c)]++
			}
			maxBucket := 0
			for _, b := range buckets {
				if b > maxBucket {
					maxBucket = b
				}
			}
			if maxBucket < bestScore {
				bestScore = maxBucket
				best = w
			}
		}
		score := master.Guess(best)
		if score == 6 {
			return
		}
		next := []string{}
		for _, c := range candidates {
			if match(c, best) == score {
				next = append(next, c)
			}
		}
		candidates = next
	}
}
