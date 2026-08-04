// LeetCode 1311 - Get Watched Videos by Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

import "sort"

func watchedVideosByFriends(watchedVideos [][]string, friends [][]int, id int, level int) []string {
	type item struct{ person, dist int }
	queue := []item{{id, 0}}
	seen := map[int]bool{id: true}
	var people []int
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.dist == level {
			people = append(people, cur.person)
			continue
		}
		for _, friend := range friends[cur.person] {
			if !seen[friend] {
				seen[friend] = true
				queue = append(queue, item{friend, cur.dist + 1})
			}
		}
	}
	counts := map[string]int{}
	for _, person := range people {
		for _, video := range watchedVideos[person] {
			counts[video]++
		}
	}
	answer := make([]string, 0, len(counts))
	for v := range counts {
		answer = append(answer, v)
	}
	sort.Slice(answer, func(i, j int) bool {
		if counts[answer[i]] != counts[answer[j]] {
			return counts[answer[i]] < counts[answer[j]]
		}
		return answer[i] < answer[j]
	})
	return answer
}
