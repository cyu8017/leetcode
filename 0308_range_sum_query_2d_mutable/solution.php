// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix {
    /** @var int[][] */
    private $matrix;
    /** @var int */
    private $rows;
    /** @var int */
    private $cols;
    /** @var int[][] */
    private $tree;

    /**
     * @param Integer[][] $matrix
     */
    function __construct($matrix) {
        $this->matrix = $matrix;
        $this->rows = count($matrix);
        $this->cols = $this->rows === 0 ? 0 : count($matrix[0]);
        $this->tree = array_fill(0, $this->rows + 1, array_fill(0, $this->cols + 1, 0));
        for ($row = 0; $row < $this->rows; $row++) {
            for ($col = 0; $col < $this->cols; $col++) {
                $this->add($row + 1, $col + 1, $matrix[$row][$col]);
            }
        }
    }

    /**
     * @param Integer $row
     * @param Integer $col
     * @param Integer $val
     * @return void
     */
    function update($row, $col, $val) {
        $delta = $val - $this->matrix[$row][$col];
        $this->matrix[$row][$col] = $val;
        $this->add($row + 1, $col + 1, $delta);
    }

    /**
     * @param Integer $row1
     * @param Integer $col1
     * @param Integer $row2
     * @param Integer $col2
     * @return Integer
     */
    function sumRegion($row1, $col1, $row2, $col2) {
        return $this->prefix($row2 + 1, $col2 + 1)
            - $this->prefix($row1, $col2 + 1)
            - $this->prefix($row2 + 1, $col1)
            + $this->prefix($row1, $col1);
    }

    /**
     * @param int $row
     * @param int $col
     * @param int $delta
     * @return void
     */
    private function add($row, $col, $delta) {
        $rowIndex = $row;
        while ($rowIndex <= $this->rows) {
            $colIndex = $col;
            while ($colIndex <= $this->cols) {
                $this->tree[$rowIndex][$colIndex] += $delta;
                $colIndex += $colIndex & -$colIndex;
            }
            $rowIndex += $rowIndex & -$rowIndex;
        }
    }

    /**
     * @param int $row
     * @param int $col
     * @return int
     */
    private function prefix($row, $col) {
        $total = 0;
        $rowIndex = $row;
        while ($rowIndex > 0) {
            $colIndex = $col;
            while ($colIndex > 0) {
                $total += $this->tree[$rowIndex][$colIndex];
                $colIndex -= $colIndex & -$colIndex;
            }
            $rowIndex -= $rowIndex & -$rowIndex;
        }
        return $total;
    }
}
