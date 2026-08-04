// LeetCode 1345 - Jump Game IV
// https://leetcode.com/problems/jump-game-iv/

func minJumps(arr []int) int {
	positions := map[int][]int{}
	for i, value := range arr {
		positions[value] = append(positions[value], i)
	}
	queue := []int{0}
	seen := map[int]bool{0: true}
	steps := 0
	for len(queue) > 0 {
		for sz := len(queue); sz > 0; sz-- {
			i := queue[0]
			queue = queue[1:]
			if i == len(arr)-1 {
				return steps
			}
			cands := append(append([]int{}, positions[arr[i]]...), i-1, i+1)
			delete(positions, arr[i])
			for _, j := range cands {
				if j >= 0 && j < len(arr) && !seen[j] {
					seen[j] = true
					queue = append(queue, j)
				}
			}
		}
		steps++
	}
	return -1
}
