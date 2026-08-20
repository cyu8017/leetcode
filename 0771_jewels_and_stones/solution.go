// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

func numJewelsInStones(jewels string, stones string) int {
	set := map[byte]bool{}
	for i := 0; i < len(jewels); i++ {
		set[jewels[i]] = true
	}
	ans := 0
	for i := 0; i < len(stones); i++ {
		if set[stones[i]] {
			ans++
		}
	}
	return ans
}
