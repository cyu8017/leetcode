// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

func minimumRecolors(blocks string, k int) int {
	white := 0
	for i := 0; i < k; i++ {
		if blocks[i] == 'W' {
			white++
		}
	}
	ans := white
	for i := k; i < len(blocks); i++ {
		if blocks[i] == 'W' {
			white++
		}
		if blocks[i-k] == 'W' {
			white--
		}
		if white < ans {
			ans = white
		}
	}
	return ans
}
