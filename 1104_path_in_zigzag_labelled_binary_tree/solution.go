// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

func pathInZigZagTree(label int) []int {
	path := []int{label}
	for label > 1 {
		level := bitsLen(label) - 1
		label >>= 1
		label = (1 << level) - 1 - label + (1 << (level - 1))
		path = append(path, label)
	}
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	return path
}

func bitsLen(x int) int {
	n := 0
	for x > 0 {
		x >>= 1
		n++
	}
	return n
}
