// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

func maxLength(arr []string) int {
	type pair struct{ used, length int }
	masks := []pair{{0, 0}}
	for _, word := range arr {
		mask := 0
		ok := true
		for i := 0; i < len(word); i++ {
			bit := 1 << (word[i] - 'a')
			if mask&bit != 0 {
				ok = false
				break
			}
			mask |= bit
		}
		if !ok || bits(mask) != len(word) {
			continue
		}
		cur := masks
		for _, p := range cur {
			if p.used&mask == 0 {
				masks = append(masks, pair{p.used | mask, p.length + len(word)})
			}
		}
	}
	best := 0
	for _, p := range masks {
		if p.length > best {
			best = p.length
		}
	}
	return best
}

func bits(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
