// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

func countTriplets(nums []int) int {
	cnt := map[int]int{}
	for _, a := range nums {
		for _, b := range nums {
			cnt[a&b]++
		}
	}
	ans := 0
	for _, c := range nums {
		for ab, times := range cnt {
			if ab&c == 0 {
				ans += times
			}
		}
	}
	return ans
}
