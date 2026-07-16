// LeetCode 0353 - Design Snake Game
class SnakeGame {
    constructor(width, height, food) {
        this.width = width;
        this.height = height;
        this.food = food;
        this.foodIndex = 0;
        this.score = 0;
        this.snake = [[0, 0]];
        this.body = new Set(["0,0"]);
    }

    move(direction) {
        let [row, col] = this.snake[0];
        if (direction === "U") row -= 1;
        else if (direction === "D") row += 1;
        else if (direction === "L") col -= 1;
        else col += 1;

        if (row < 0 || row >= this.height || col < 0 || col >= this.width) return -1;

        const willEat = this.foodIndex < this.food.length
            && row === this.food[this.foodIndex][0]
            && col === this.food[this.foodIndex][1];

        if (!willEat) {
            const [tailRow, tailCol] = this.snake.pop();
            this.body.delete(`${tailRow},${tailCol}`);
        }

        const key = `${row},${col}`;
        if (this.body.has(key)) return -1;

        this.snake.unshift([row, col]);
        this.body.add(key);

        if (willEat) {
            this.score += 1;
            this.foodIndex += 1;
        }

        return this.score;
    }
}

module.exports = { SnakeGame };
