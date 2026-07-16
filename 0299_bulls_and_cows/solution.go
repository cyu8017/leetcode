// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

import "fmt"

func getHint(secret string, guess string) string {
	bulls := 0
	secretCounts := make(map[byte]int)
	guessCounts := make(map[byte]int)

	for index := 0; index < len(secret); index++ {
		if secret[index] == guess[index] {
			bulls++
		} else {
			secretCounts[secret[index]]++
			guessCounts[guess[index]]++
		}
	}

	cows := 0
	for digit, guessCount := range guessCounts {
		secretCount := secretCounts[digit]
		if guessCount < secretCount {
			cows += guessCount
		} else {
			cows += secretCount
		}
	}

	return fmt.Sprintf("%dA%dB", bulls, cows)
}
