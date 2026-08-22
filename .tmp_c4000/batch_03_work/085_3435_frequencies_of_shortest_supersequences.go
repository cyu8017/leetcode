// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

func supersequences(words []string) [][]int {
	// words length 2 each - graph of letter constraints
	need := [26][26]bool{}
	used := [26]bool{}
	for _, w := range words {
		a, b := w[0]-'a', w[1]-'a'
		used[a] = true
		used[b] = true
		if a != b {
			need[a][b] = true
		}
	}
	letters := []int{}
	for i := 0; i < 26; i++ {
		if used[i] {
			letters = append(letters, i)
		}
	}
	m := len(letters)
	best := int(1e9)
	var bestFreqs [][]int
	var dfs func(i int, freq [26]int)
	dfs = func(i int, freq [26]int) {
		if i == m {
			// validate: for each word, can form as subsequence with freqs
			ok := true
			for _, w := range words {
				a, b := int(w[0]-'a'), int(w[1]-'a')
				if a == b {
					if freq[a] < 2 {
						ok = false
						break
					}
				} else if freq[a] < 1 || freq[b] < 1 {
					ok = false
					break
				}
			}
			if !ok {
				return
			}
			sum := 0
			f := make([]int, 26)
			for j := 0; j < 26; j++ {
				f[j] = freq[j]
				sum += freq[j]
			}
			if sum < best {
				best = sum
				bestFreqs = [][]int{f}
			} else if sum == best {
				bestFreqs = append(bestFreqs, f)
			}
			return
		}
		L := letters[i]
		for c := 1; c <= 2; c++ {
			freq[L] = c
			dfs(i+1, freq)
		}
		freq[L] = 0
	}
	dfs(0, [26]int{})
	return bestFreqs
}
