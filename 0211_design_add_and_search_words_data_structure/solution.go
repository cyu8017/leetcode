// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

type TrieNode struct {
	children map[byte]*TrieNode
	isWord   bool
}

type WordDictionary struct {
	root *TrieNode
}

func Constructor() WordDictionary {
	return WordDictionary{root: &TrieNode{children: map[byte]*TrieNode{}}}
}

func (this *WordDictionary) AddWord(word string) {
	node := this.root
	for i := 0; i < len(word); i++ {
		c := word[i]
		if node.children[c] == nil {
			node.children[c] = &TrieNode{children: map[byte]*TrieNode{}}
		}
		node = node.children[c]
	}
	node.isWord = true
}

func (this *WordDictionary) Search(word string) bool {
	var dfs func(node *TrieNode, index int) bool
	dfs = func(node *TrieNode, index int) bool {
		if index == len(word) {
			return node.isWord
		}
		c := word[index]
		if c == '.' {
			for _, child := range node.children {
				if dfs(child, index+1) {
					return true
				}
			}
			return false
		}
		next := node.children[c]
		if next == nil {
			return false
		}
		return dfs(next, index+1)
	}
	return dfs(this.root, 0)
}
