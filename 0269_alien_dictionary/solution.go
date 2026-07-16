// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

import "strings"

func alienOrder(words []string) string {
	graph := make(map[rune]map[rune]bool)
	indegree := make(map[rune]int)

	for _, word := range words {
		for _, char := range word {
			if _, ok := graph[char]; !ok {
				graph[char] = make(map[rune]bool)
				indegree[char] = 0
			}
		}
	}

	for i := 0; i < len(words)-1; i++ {
		first := words[i]
		second := words[i+1]
		if len(first) > len(second) && strings.HasPrefix(first, second) {
			return ""
		}
		limit := len(first)
		if len(second) < limit {
			limit = len(second)
		}
		for j := 0; j < limit; j++ {
			left := rune(first[j])
			right := rune(second[j])
			if left != right {
				if !graph[left][right] {
					graph[left][right] = true
					indegree[right]++
				}
				break
			}
		}
	}

	queue := make([]rune, 0)
	for char, degree := range indegree {
		if degree == 0 {
			queue = append(queue, char)
		}
	}

	order := make([]rune, 0, len(indegree))
	for len(queue) > 0 {
		char := queue[0]
		queue = queue[1:]
		order = append(order, char)
		for next := range graph[char] {
			indegree[next]--
			if indegree[next] == 0 {
				queue = append(queue, next)
			}
		}
	}

	if len(order) != len(indegree) {
		return ""
	}
	return string(order)
}
