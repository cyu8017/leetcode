// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix {
    /** @var int[][] */
    private $prefix;

    /**
     * @param Integer[][] $matrix
     */
    function __construct($matrix) {
        $rows = count($matrix);
        $cols = $rows === 0 ? 0 : count($matrix[0]);
        $this->prefix = array_fill(0, $rows + 1, array_fill(0, $cols + 1, 0));
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                $this->prefix[$row + 1][$col + 1] = $matrix[$row][$col]
                    + $this->prefix[$row][$col + 1]
                    + $this->prefix[$row + 1][$col]
                    - $this->prefix[$row][$col];
            }
        }
    }

    /**
     * @param Integer $row1
     * @param Integer $col1
     * @param Integer $row2
     * @param Integer $col2
     * @return Integer
     */
    function sumRegion($row1, $col1, $row2, $col2) {
        $topLeft = $this->prefix[$row1][$col1];
        $topRight = $this->prefix[$row1][$col2 + 1];
        $bottomLeft = $this->prefix[$row2 + 1][$col1];
        $bottomRight = $this->prefix[$row2 + 1][$col2 + 1];
        return $bottomRight - $topRight - $bottomLeft + $topLeft;
    }
}
