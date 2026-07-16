// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree
// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

import "strings"

func isValidSerialization(preorder string) bool {
	slots := 1
	for _, node := range strings.Split(preorder, ",") {
		slots -= 1
		if slots < 0 {
			return false
		}
		if node != "#" {
			slots += 2
		}
	}
	return slots == 0
}
