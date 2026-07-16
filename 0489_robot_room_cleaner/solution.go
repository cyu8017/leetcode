// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

type Robot interface {
	Move() bool
	TurnLeft()
	TurnRight()
	Clean()
}

type Solution struct{}

func (Solution) CleanRoom(robot Robot) {
	visited := map[[3]int]bool{}
	directions := [4][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
	var backtrack func(row, col, direction int)
	backtrack = func(row, col, direction int) {
		robot.Clean()
		for step := 0; step < 4; step++ {
			nextDirection := (direction + step) % 4
			nextRow := row + directions[nextDirection][0]
			nextCol := col + directions[nextDirection][1]
			state := [3]int{nextRow, nextCol, nextDirection}
			if !visited[state] && robot.Move() {
				visited[state] = true
				backtrack(nextRow, nextCol, nextDirection)
				robot.TurnRight()
				robot.TurnRight()
				robot.Move()
				robot.TurnRight()
				robot.TurnRight()
			}
			robot.TurnRight()
		}
	}
	visited[[3]int{0, 0, 0}] = true
	backtrack(0, 0, 0)
}
