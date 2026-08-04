// LeetCode 1523 - Count Odd Numbers in an Interval Range
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

func countOdds(low int, high int) int {
	return (high+1)/2 - low/2
}
