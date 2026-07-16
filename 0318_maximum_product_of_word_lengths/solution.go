// LeetCode 0318 - Maximum Product of Word Lengths
// https://leetcode.com/problems/maximum-product-of-word-lengths/

func maxProduct(words []string) int {
	masks := make([]int, len(words))
	lengths := make([]int, len(words))

	for index, word := range words {
		mask := 0
		valid := true
		for _, character := range word {
			bit := 1 << (character - 'a')
			if mask&bit != 0 {
				valid = false
				break
			}
			mask |= bit
		}
		if !valid {
			mask = 0
		}
		masks[index] = mask
		lengths[index] = len(word)
	}

	best := 0
	for left := 0; left < len(words); left++ {
		if masks[left] == 0 {
			continue
		}
		for right := left + 1; right < len(words); right++ {
			if masks[right] == 0 {
				continue
			}
			if masks[left]&masks[right] == 0 && lengths[left]*lengths[right] > best {
				best = lengths[left] * lengths[right]
			}
		}
	}

	return best
}
