// LeetCode 0245 - Shortest Word Distance III
// https://leetcode.com/problems/shortest-word-distance-iii/

func shortestWordDistance(wordsDict []string, word1 string, word2 string) int {
	if word1 == word2 {
		previous := -1
		best := int(^uint(0) >> 1)
		for index, word := range wordsDict {
			if word == word1 {
				if previous >= 0 {
					if index-previous < best {
						best = index - previous
					}
				}
				previous = index
			}
		}
		return best
	}

	index1 := -1
	index2 := -1
	best := int(^uint(0) >> 1)
	for index, word := range wordsDict {
		if word == word1 {
			index1 = index
			if index2 >= 0 {
				if index-index2 < best {
					best = index - index2
				}
			}
		}
		if word == word2 {
			index2 = index
			if index1 >= 0 {
				if index-index1 < best {
					best = index - index1
				}
			}
		}
	}
	return best
}
