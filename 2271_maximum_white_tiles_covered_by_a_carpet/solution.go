// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

import "sort"

func maximumWhiteTiles(tiles [][]int, carpetLen int) int {
	sort.Slice(tiles, func(i, j int) bool { return tiles[i][0] < tiles[j][0] })
	n := len(tiles)
	pref := make([]int, n+1)
	for i, t := range tiles {
		pref[i+1] = pref[i] + (t[1] - t[0] + 1)
	}
	ans := 0
	j := 0
	for i := 0; i < n; i++ {
		end := tiles[i][0] + carpetLen - 1
		for j < n && tiles[j][0] <= end {
			j++
		}
		cover := pref[j] - pref[i]
		if j > 0 && tiles[j-1][1] > end {
			cover -= tiles[j-1][1] - end
		}
		if cover > ans {
			ans = cover
		}
	}
	return ans
}
