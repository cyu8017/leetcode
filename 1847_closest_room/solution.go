// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

import "sort"

func closestRoom(rooms [][]int, queries [][]int) []int {
	sort.Slice(rooms, func(i, j int) bool {
		return rooms[i][1] < rooms[j][1]
	})

	type indexedQuery struct {
		index     int
		preferred int
		minSize   int
	}

	indexed := make([]indexedQuery, len(queries))
	for i, query := range queries {
		indexed[i] = indexedQuery{i, query[0], query[1]}
	}
	sort.Slice(indexed, func(i, j int) bool {
		return indexed[i].minSize > indexed[j].minSize
	})

	available := make([]int, 0)
	roomIndex := len(rooms) - 1
	answer := make([]int, len(queries))
	for i := range answer {
		answer[i] = -1
	}

	for _, query := range indexed {
		for roomIndex >= 0 && rooms[roomIndex][1] >= query.minSize {
			roomID := rooms[roomIndex][0]
			pos := sort.SearchInts(available, roomID)
			available = append(available, 0)
			copy(available[pos+1:], available[pos:])
			available[pos] = roomID
			roomIndex--
		}

		if len(available) == 0 {
			continue
		}

		pos := sort.SearchInts(available, query.preferred)
		bestID := -1
		bestDist := int(^uint(0) >> 1)

		if pos < len(available) {
			roomID := available[pos]
			dist := absInt(roomID - query.preferred)
			if dist < bestDist || (dist == bestDist && roomID < bestID) {
				bestID = roomID
				bestDist = dist
			}
		}
		if pos > 0 {
			roomID := available[pos-1]
			dist := absInt(roomID - query.preferred)
			if dist < bestDist || (dist == bestDist && roomID < bestID) {
				bestID = roomID
			}
		}

		answer[query.index] = bestID
	}

	return answer
}

func absInt(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
