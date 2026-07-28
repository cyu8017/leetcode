// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

func numTilePossibilities(tiles string) int {
	count := map[byte]int{}
	for i := 0; i < len(tiles); i++ {
		count[tiles[i]]++
	}
	var dfs func() int
	dfs = func() int {
		total := 0
		for ch, freq := range count {
			if freq == 0 {
				continue
			}
			count[ch]--
			total += 1 + dfs()
			count[ch]++
		}
		return total
	}
	return dfs()
}
