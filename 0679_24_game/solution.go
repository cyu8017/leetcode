// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

func judgePoint24(cards []int) bool {
	const eps = 1e-6
	var dfs func(nums []float64) bool
	dfs = func(nums []float64) bool {
		if len(nums) == 1 {
			if nums[0]-24 < 0 {
				return 24-nums[0] < eps
			}
			return nums[0]-24 < eps
		}
		for i := 0; i < len(nums); i++ {
			for j := 0; j < len(nums); j++ {
				if i == j {
					continue
				}
				rest := []float64{}
				for k := 0; k < len(nums); k++ {
					if k != i && k != j {
						rest = append(rest, nums[k])
					}
				}
				a, b := nums[i], nums[j]
				candidates := []float64{a + b, a - b, a * b}
				if b > eps || b < -eps {
					candidates = append(candidates, a/b)
				}
				for _, value := range candidates {
					if dfs(append(append([]float64{}, rest...), value)) {
						return true
					}
				}
			}
		}
		return false
	}
	nums := make([]float64, len(cards))
	for i, x := range cards {
		nums[i] = float64(x)
	}
	return dfs(nums)
}
