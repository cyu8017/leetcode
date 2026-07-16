// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer[]
     */
    function spiralOrder($matrix) {
        if (count($matrix) === 0) {
            return [];
        }

        $top = 0;
        $bottom = count($matrix) - 1;
        $left = 0;
        $right = count($matrix[0]) - 1;
        $result = [];

        while ($top <= $bottom && $left <= $right) {
            for ($col = $left; $col <= $right; $col++) {
                $result[] = $matrix[$top][$col];
            }
            $top++;

            for ($row = $top; $row <= $bottom; $row++) {
                $result[] = $matrix[$row][$right];
            }
            $right--;

            if ($top <= $bottom) {
                for ($col = $right; $col >= $left; $col--) {
                    $result[] = $matrix[$bottom][$col];
                }
                $bottom--;
            }

            if ($left <= $right) {
                for ($row = $bottom; $row >= $top; $row--) {
                    $result[] = $matrix[$row][$left];
                }
                $left++;
            }
        }

        return $result;
    }
}
