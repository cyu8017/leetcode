package main
// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

import (
	"sort"
	"strconv"
	"strings"
)

func earliestAndLatest(n int, firstPlayer int, secondPlayer int) []int {
	first := firstPlayer
	second := secondPlayer
	memo := map[string][2]int{}

	encode := func(players []int) string {
		parts := make([]string, len(players))
		for i, player := range players {
			parts[i] = strconv.Itoa(player)
		}
		return strings.Join(parts, ",")
	}

	var dfs func([]int) [2]int
	dfs = func(players []int) [2]int {
		key := encode(players)
		if value, ok := memo[key]; ok {
			return value
		}

		count := len(players)
		firstIndex := -1
		secondIndex := -1
		for index, player := range players {
			if player == first {
				firstIndex = index
			}
			if player == second {
				secondIndex = index
			}
		}
		if firstIndex+secondIndex == count-1 {
			return [2]int{1, 1}
		}

		choices := make([][]int, 0, count/2+1)
		for index := 0; index < count/2; index++ {
			left := players[index]
			right := players[count-1-index]
			if left == first || left == second {
				choices = append(choices, []int{left})
			} else if right == first || right == second {
				choices = append(choices, []int{right})
			} else {
				choices = append(choices, []int{left, right})
			}
		}
		if count%2 == 1 {
			choices = append(choices, []int{players[count/2]})
		}

		earliest := 1000000000
		latest := 0
		var walk func(int, []int)
		walk = func(depth int, picks []int) {
			if depth == len(choices) {
				winners := append([]int(nil), picks...)
				sort.Ints(winners)
				result := dfs(winners)
				early := result[0] + 1
				late := result[1] + 1
				if early < earliest {
					earliest = early
				}
				if late > latest {
					latest = late
				}
				return
			}
			for _, pick := range choices[depth] {
				walk(depth+1, append(picks, pick))
			}
		}
		walk(0, nil)

		value := [2]int{earliest, latest}
		memo[key] = value
		return value
	}

	players := make([]int, n)
	for i := 0; i < n; i++ {
		players[i] = i + 1
	}
	result := dfs(players)
	return []int{result[0], result[1]}
}
func main() {}
