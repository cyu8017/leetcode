// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

type TrieNode struct {
	children map[byte]*TrieNode
	word     string
}

func findWords(board [][]byte, words []string) []string {
	root := &TrieNode{children: map[byte]*TrieNode{}}
	for _, word := range words {
		node := root
		for i := 0; i < len(word); i++ {
			c := word[i]
			if node.children[c] == nil {
				node.children[c] = &TrieNode{children: map[byte]*TrieNode{}}
			}
			node = node.children[c]
		}
		node.word = word
	}

	rows, cols := len(board), len(board[0])
	result := map[string]struct{}{}

	var dfs func(row, col int, node *TrieNode)
	dfs = func(row, col int, node *TrieNode) {
		c := board[row][col]
		next := node.children[c]
		if next == nil {
			return
		}
		if next.word != "" {
			result[next.word] = struct{}{}
			next.word = ""
		}
		board[row][col] = '#'
		if row+1 < rows && board[row+1][col] != '#' {
			dfs(row+1, col, next)
		}
		if row-1 >= 0 && board[row-1][col] != '#' {
			dfs(row-1, col, next)
		}
		if col+1 < cols && board[row][col+1] != '#' {
			dfs(row, col+1, next)
		}
		if col-1 >= 0 && board[row][col-1] != '#' {
			dfs(row, col-1, next)
		}
		board[row][col] = c
		if len(next.children) == 0 {
			delete(node.children, c)
		}
	}

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			dfs(row, col, root)
		}
	}

	answer := make([]string, 0, len(result))
	for word := range result {
		answer = append(answer, word)
	}
	return answer
}
