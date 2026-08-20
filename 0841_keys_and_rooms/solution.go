// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

func canVisitAllRooms(rooms [][]int) bool {
	seen := map[int]bool{0: true}
	stack := []int{0}
	for len(stack) > 0 {
		room := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, key := range rooms[room] {
			if !seen[key] {
				seen[key] = true
				stack = append(stack, key)
			}
		}
	}
	return len(seen) == len(rooms)
}
