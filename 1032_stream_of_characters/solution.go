// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

type trieNode1032 struct {
	children [26]*trieNode1032
	isWord   bool
}

type StreamChecker struct {
	root   *trieNode1032
	stream []byte
}

func Constructor(words []string) StreamChecker {
	root := &trieNode1032{}
	for _, word := range words {
		node := root
		for i := len(word) - 1; i >= 0; i-- {
			idx := word[i] - 'a'
			if node.children[idx] == nil {
				node.children[idx] = &trieNode1032{}
			}
			node = node.children[idx]
		}
		node.isWord = true
	}
	return StreamChecker{root: root}
}

func (this *StreamChecker) Query(letter byte) bool {
	this.stream = append(this.stream, letter)
	node := this.root
	for i := len(this.stream) - 1; i >= 0; i-- {
		if node.isWord {
			return true
		}
		idx := this.stream[i] - 'a'
		if node.children[idx] == nil {
			return false
		}
		node = node.children[idx]
	}
	return node.isWord
}
