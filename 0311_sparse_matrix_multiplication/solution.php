// LeetCode 0311 - Sparse Matrix Multiplication
// https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution {
    /**
     * @param Integer[][] $mat1
     * @param Integer[][] $mat2
     * @return Integer[][]
     */
    function multiply($mat1, $mat2) {
        $rows = count($mat1);
        $inner = count($mat1[0]);
        $cols = count($mat2[0]);
        $result = array_fill(0, $rows, array_fill(0, $cols, 0));
        for ($row = 0; $row < $rows; $row++) {
            for ($index = 0; $index < $inner; $index++) {
                if ($mat1[$row][$index] === 0) {
                    continue;
                }
                for ($col = 0; $col < $cols; $col++) {
                    if ($mat2[$index][$col] !== 0) {
                        $result[$row][$col] += $mat1[$row][$index] * $mat2[$index][$col];
                    }
                }
            }
        }
        return $result;
    }
}
