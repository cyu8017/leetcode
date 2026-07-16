// LeetCode 0073 - Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function setZeroes(&$matrix) {
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $firstRowZero = false;
        $firstColZero = false;

        for ($j = 0; $j < $cols; $j++) {
            if ($matrix[0][$j] === 0) {
                $firstRowZero = true;
                break;
            }
        }
        for ($i = 0; $i < $rows; $i++) {
            if ($matrix[$i][0] === 0) {
                $firstColZero = true;
                break;
            }
        }

        for ($i = 1; $i < $rows; $i++) {
            for ($j = 1; $j < $cols; $j++) {
                if ($matrix[$i][$j] === 0) {
                    $matrix[$i][0] = 0;
                    $matrix[0][$j] = 0;
                }
            }
        }

        for ($i = 1; $i < $rows; $i++) {
            for ($j = 1; $j < $cols; $j++) {
                if ($matrix[$i][0] === 0 || $matrix[0][$j] === 0) {
                    $matrix[$i][$j] = 0;
                }
            }
        }

        if ($firstRowZero) {
            for ($j = 0; $j < $cols; $j++) {
                $matrix[0][$j] = 0;
            }
        }
        if ($firstColZero) {
            for ($i = 0; $i < $rows; $i++) {
                $matrix[$i][0] = 0;
            }
        }
    }
}
