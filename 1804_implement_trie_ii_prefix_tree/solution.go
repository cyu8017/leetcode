// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

type trieNode struct {
	children    map[byte]*trieNode
	wordCount   int
	prefixCount int
}

type Trie struct {
	root *trieNode
}

func Constructor() Trie {
	return Trie{root: &trieNode{children: make(map[byte]*trieNode)}}
}

func (t *Trie) Insert(word string) {
	node := t.root
	for i := 0; i < len(word); i++ {
		ch := word[i]
		if node.children[ch] == nil {
			node.children[ch] = &trieNode{children: make(map[byte]*trieNode)}
		}
		node = node.children[ch]
		node.prefixCount++
	}
	node.wordCount++
}

func (t *Trie) find(text string) *trieNode {
	node := t.root
	for i := 0; i < len(text); i++ {
		node = node.children[text[i]]
		if node == nil {
			return nil
		}
	}
	return node
}

func (t *Trie) CountWordsEqualTo(word string) int {
	node := t.find(word)
	if node == nil {
		return 0
	}
	return node.wordCount
}

func (t *Trie) CountWordsStartingWith(prefix string) int {
	node := t.find(prefix)
	if node == nil {
		return 0
	}
	return node.prefixCount
}

func (t *Trie) Erase(word string) {
	node := t.root
	for i := 0; i < len(word); i++ {
		node = node.children[word[i]]
		node.prefixCount--
	}
	node.wordCount--
}
