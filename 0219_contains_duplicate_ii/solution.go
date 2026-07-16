// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

func containsNearbyDuplicate(nums []int, k int) bool {
	lastIndex := make(map[int]int, len(nums))
	for i, num := range nums {
		if prev, ok := lastIndex[num]; ok && i-prev <= k {
			return true
		}
		lastIndex[num] = i
	}
	return false
}
