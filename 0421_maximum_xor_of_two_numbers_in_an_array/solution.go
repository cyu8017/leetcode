// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

func findMaximumXOR(nums []int) int {
	maximum := nums[0]
	for _, value := range nums[1:] {
		if value > maximum {
			maximum = value
		}
	}

	maxBit := 0
	for (1 << maxBit) <= maximum && maxBit < 31 {
		maxBit++
	}

	type trieNode struct {
		children [2]int
	}
	nodes := []trieNode{{}}
	nextID := func() int {
		nodes = append(nodes, trieNode{})
		return len(nodes) - 1
	}

	for _, number := range nums {
		node := 0
		for bit := maxBit - 1; bit >= 0; bit-- {
			current := (number >> bit) & 1
			if nodes[node].children[current] == 0 {
				nodes[node].children[current] = nextID()
			}
			node = nodes[node].children[current]
		}
	}

	best := 0
	for _, number := range nums {
		node := 0
		candidate := 0
		for bit := maxBit - 1; bit >= 0; bit-- {
			current := (number >> bit) & 1
			target := 1 - current
			if nodes[node].children[target] != 0 {
				candidate |= 1 << bit
				node = nodes[node].children[target]
			} else {
				node = nodes[node].children[current]
			}
		}
		if candidate > best {
			best = candidate
		}
	}

	return best
}
