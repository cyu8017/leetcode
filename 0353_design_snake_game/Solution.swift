// LeetCode 0353 - Design Snake Game
// https://leetcode.com/problems/design-snake-game/

class SnakeGame {
    private let width: Int
    private let height: Int
    private let food: [[Int]]
    private var foodIndex = 0
    private var score = 0
    private var snake: [[Int]]
    private var body: Set<String>

    init(_ width: Int, _ height: Int, _ food: [[Int]]) {
        self.width = width
        self.height = height
        self.food = food
        self.snake = [[0, 0]]
        self.body = ["0,0"]
    }

    func move(_ direction: String) -> Int {
        var row = snake[0][0]
        var col = snake[0][1]

        switch direction {
        case "U":
            row -= 1
        case "D":
            row += 1
        case "L":
            col -= 1
        default:
            col += 1
        }

        if row < 0 || row >= height || col < 0 || col >= width {
            return -1
        }

        let willEat = foodIndex < food.count
            && row == food[foodIndex][0]
            && col == food[foodIndex][1]

        if !willEat {
            let tail = snake.removeLast()
            body.remove("\(tail[0]),\(tail[1])")
        }

        let headKey = "\(row),\(col)"
        if body.contains(headKey) {
            return -1
        }

        snake.insert([row, col], at: 0)
        body.insert(headKey)

        if willEat {
            score += 1
            foodIndex += 1
        }

        return score
    }
}
