// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

func pathSum(nums []int) int {
	tree := map[[2]int]int{}
	for _, num := range nums {
		depth, pos, val := num/100, (num/10)%10, num%10
		tree[[2]int{depth, pos}] = val
	}
	total := 0
	var dfs func(depth, pos, path int)
	dfs = func(depth, pos, path int) {
		key := [2]int{depth, pos}
		if _, ok := tree[key]; !ok {
			return
		}
		path += tree[key]
		left := [2]int{depth + 1, pos*2 - 1}
		right := [2]int{depth + 1, pos * 2}
		_, hasL := tree[left]
		_, hasR := tree[right]
		if !hasL && !hasR {
			total += path
			return
		}
		dfs(depth+1, pos*2-1, path)
		dfs(depth+1, pos*2, path)
	}
	dfs(1, 1, 0)
	return total
}
