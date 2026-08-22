// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

import (
	"strconv"
	"strings"
)

func palindromicPathQueries(n int, edges [][]int, s string, queries []string) []bool {
	graph := make([][]int, n)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], edge[1])
		graph[edge[1]] = append(graph[edge[1]], edge[0])
	}
	parent, depth := make([]int, n), make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	parent[0] = -1
	order := []int{0}
	for i := 0; i < len(order); i++ {
		u := order[i]
		for _, v := range graph[u] {
			if parent[v] == -2 {
				parent[v] = u
				depth[v] = depth[u] + 1
				order = append(order, v)
			}
		}
	}
	size, heavy := make([]int, n), make([]int, n)
	for i := range heavy {
		heavy[i] = -1
	}
	for i := n - 1; i >= 0; i-- {
		u := order[i]
		size[u] = 1
		for _, v := range graph[u] {
			if parent[v] == u {
				size[u] += size[v]
				if heavy[u] == -1 || size[v] > size[heavy[u]] {
					heavy[u] = v
				}
			}
		}
	}
	head, position := make([]int, n), make([]int, n)
	type chain3841 struct{ node, head int }
	stack := []chain3841{{0, 0}}
	nextPosition := 0
	for len(stack) > 0 {
		chain := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for u := chain.node; u != -1; u = heavy[u] {
			head[u], position[u] = chain.head, nextPosition
			nextPosition++
			for _, v := range graph[u] {
				if parent[v] == u && v != heavy[u] {
					stack = append(stack, chain3841{v, v})
				}
			}
		}
	}
	bit := make([]int, n+1)
	update := func(index, value int) {
		for index++; index <= n; index += index & -index {
			bit[index] ^= value
		}
	}
	prefix := func(index int) int {
		result := 0
		for index > 0 {
			result ^= bit[index]
			index -= index & -index
		}
		return result
	}
	pathMask := func(u, v int) int {
		result := 0
		for head[u] != head[v] {
			if depth[head[u]] < depth[head[v]] {
				u, v = v, u
			}
			result ^= prefix(position[u]+1) ^ prefix(position[head[u]])
			u = parent[head[u]]
		}
		if position[u] > position[v] {
			u, v = v, u
		}
		return result ^ prefix(position[v]+1) ^ prefix(position[u])
	}
	current := []byte(s)
	for node, character := range current {
		update(position[node], 1<<int(character-'a'))
	}
	answer := make([]bool, 0)
	for _, query := range queries {
		fields := strings.Fields(query)
		node, _ := strconv.Atoi(fields[1])
		if fields[0] == "update" {
			newCharacter := fields[2][0]
			delta := (1 << int(current[node]-'a')) ^ (1 << int(newCharacter-'a'))
			update(position[node], delta)
			current[node] = newCharacter
			continue
		}
		other, _ := strconv.Atoi(fields[2])
		mask := pathMask(node, other)
		answer = append(answer, mask&(mask-1) == 0)
	}
	return answer
}