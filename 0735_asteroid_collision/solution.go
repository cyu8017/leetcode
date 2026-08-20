// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

func asteroidCollision(asteroids []int) []int {
	stack := []int{}
	for _, asteroid := range asteroids {
		alive := true
		for alive && len(stack) > 0 && asteroid < 0 && stack[len(stack)-1] > 0 {
			if stack[len(stack)-1] < -asteroid {
				stack = stack[:len(stack)-1]
				continue
			}
			if stack[len(stack)-1] == -asteroid {
				stack = stack[:len(stack)-1]
			}
			alive = false
		}
		if alive {
			stack = append(stack, asteroid)
		}
	}
	return stack
}
