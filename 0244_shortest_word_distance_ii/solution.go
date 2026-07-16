// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

type WordDistance struct {
	positions map[string][]int
}

func Constructor(wordsDict []string) WordDistance {
	positions := make(map[string][]int)
	for index, word := range wordsDict {
		positions[word] = append(positions[word], index)
	}
	return WordDistance{positions: positions}
}

func (this *WordDistance) Shortest(word1 string, word2 string) int {
	left := this.positions[word1]
	right := this.positions[word2]
	i := 0
	j := 0
	best := int(^uint(0) >> 1)
	for i < len(left) && j < len(right) {
		distance := left[i] - right[j]
		if distance < 0 {
			distance = -distance
		}
		if distance < best {
			best = distance
		}
		if left[i] <= right[j] {
			i++
		} else {
			j++
		}
	}
	return best
}
