// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

func killProcess(pid []int, ppid []int, kill int) []int {
	children := map[int][]int{}
	for i, child := range pid {
		parent := ppid[i]
		children[parent] = append(children[parent], child)
	}
	result := []int{}
	queue := []int{kill}
	for len(queue) > 0 {
		process := queue[0]
		queue = queue[1:]
		result = append(result, process)
		queue = append(queue, children[process]...)
	}
	return result
}
