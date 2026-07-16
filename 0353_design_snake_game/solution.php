// LeetCode 0353 - Design Snake Game
// https://leetcode.com/problems/design-snake-game/

class SnakeGame {
    private int $width;
    private int $height;
    /** @var int[][] */
    private array $food;
    private int $foodIndex = 0;
    private int $score = 0;
    /** @var int[][] */
    private array $snake;
    /** @var array<string, bool> */
    private array $body;

    /**
     * @param int $width
     * @param int $height
     * @param int[][] $food
     */
    function __construct(int $width, int $height, array $food) {
        $this->width = $width;
        $this->height = $height;
        $this->food = $food;
        $this->snake = [[0, 0]];
        $this->body = ['0,0' => true];
    }

    function move(string $direction): int {
        $row = $this->snake[0][0];
        $col = $this->snake[0][1];

        if ($direction === 'U') {
            $row--;
        } elseif ($direction === 'D') {
            $row++;
        } elseif ($direction === 'L') {
            $col--;
        } else {
            $col++;
        }

        if ($row < 0 || $row >= $this->height || $col < 0 || $col >= $this->width) {
            return -1;
        }

        $willEat = $this->foodIndex < count($this->food)
            && $row === $this->food[$this->foodIndex][0]
            && $col === $this->food[$this->foodIndex][1];

        if (!$willEat) {
            $tail = array_pop($this->snake);
            unset($this->body[$tail[0] . ',' . $tail[1]]);
        }

        $headKey = $row . ',' . $col;
        if (array_key_exists($headKey, $this->body)) {
            return -1;
        }

        array_unshift($this->snake, [$row, $col]);
        $this->body[$headKey] = true;

        if ($willEat) {
            $this->score++;
            $this->foodIndex++;
        }

        return $this->score;
    }
}
