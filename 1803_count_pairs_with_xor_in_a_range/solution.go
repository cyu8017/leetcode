// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

type xorTrieNode struct {
	count    int
	children [2]*xorTrieNode
}

func countPairs(nums []int, low, high int) int {
	return countSmallerThan(nums, high+1) - countSmallerThan(nums, low)
}

func countSmallerThan(nums []int, limit int) int {
	if limit <= 0 {
		return 0
	}

	root := &xorTrieNode{}
	total := 0
	maxBit := 15

	for _, num := range nums {
		total += queryXorTrie(root, num, limit, maxBit)
		insertXorTrie(root, num, maxBit)
	}
	return total
}

func insertXorTrie(root *xorTrieNode, num, bit int) {
	node := root
	for i := bit; i >= 0; i-- {
		b := (num >> i) & 1
		if node.children[b] == nil {
			node.children[b] = &xorTrieNode{}
		}
		node = node.children[b]
		node.count++
	}
}

func queryXorTrie(root *xorTrieNode, num, limit, bit int) int {
	if root == nil || bit < 0 {
		return 0
	}

	numBit := (num >> bit) & 1
	limitBit := (limit >> bit) & 1
	child := root.children[numBit]

	if limitBit == 1 {
		result := 0
		if child != nil {
			result = child.count
		}
		other := root.children[1-numBit]
		result += queryXorTrie(other, num, limit, bit-1)
		return result
	}
	return queryXorTrie(child, num, limit, bit-1)
}
