// LeetCode 0353 - Design Snake Game
// https://leetcode.com/problems/design-snake-game/

type SnakeGame struct {
	width      int
	height     int
	food       [][]int
	foodIndex  int
	score      int
	snake      [][2]int
	body       map[[2]int]bool
}

func Constructor(width int, height int, food [][]int) SnakeGame {
	game := SnakeGame{
		width:  width,
		height: height,
		food:   food,
		snake:  [][2]int{{0, 0}},
		body:   map[[2]int]bool{{0, 0}: true},
	}
	return game
}

func (this *SnakeGame) Move(direction string) int {
	row, col := this.snake[0][0], this.snake[0][1]
	switch direction {
	case "U":
		row--
	case "D":
		row++
	case "L":
		col--
	default:
		col++
	}

	if row < 0 || row >= this.height || col < 0 || col >= this.width {
		return -1
	}

	willEat := this.foodIndex < len(this.food) &&
		row == this.food[this.foodIndex][0] &&
		col == this.food[this.foodIndex][1]

	if !willEat {
		tail := this.snake[len(this.snake)-1]
		this.snake = this.snake[:len(this.snake)-1]
		delete(this.body, tail)
	}

	head := [2]int{row, col}
	if this.body[head] {
		return -1
	}

	this.snake = append([][2]int{head}, this.snake...)
	this.body[head] = true

	if willEat {
		this.score++
		this.foodIndex++
	}

	return this.score
}
