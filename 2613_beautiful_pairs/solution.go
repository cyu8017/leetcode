// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/


func beautifulPair(nums1 []int, nums2 []int) []int {
	n := len(nums1)
	bestDist := int(1e18)
	ans := []int{0, 1}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			d := abs2613(nums1[i]-nums1[j]) + abs2613(nums2[i]-nums2[j])
			if d < bestDist || (d == bestDist && (i < ans[0] || (i == ans[0] && j < ans[1]))) {
				bestDist = d
				ans = []int{i, j}
			}
		}
	}
	return ans
}
func abs2613(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
