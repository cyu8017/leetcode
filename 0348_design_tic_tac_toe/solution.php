// LeetCode 0348 - Design Tic-Tac-Toe
// https://leetcode.com/problems/design-tic-tac-toe/

class TicTacToe {
    private int $n;
    private array $rows;
    private array $cols;
    private int $diag = 0;
    private int $antiDiag = 0;

    function __construct(int $n) {
        $this->n = $n;
        $this->rows = array_fill(0, $n, 0);
        $this->cols = array_fill(0, $n, 0);
    }

    function move(int $row, int $col, int $player): int {
        $add = $player === 1 ? 1 : -1;

        $this->rows[$row] += $add;
        $this->cols[$col] += $add;
        if ($row === $col) {
            $this->diag += $add;
        }
        if ($row + $col === $this->n - 1) {
            $this->antiDiag += $add;
        }

        if (
            abs($this->rows[$row]) === $this->n ||
            abs($this->cols[$col]) === $this->n ||
            abs($this->diag) === $this->n ||
            abs($this->antiDiag) === $this->n
        ) {
            return $player;
        }

        return 0;
    }
}
