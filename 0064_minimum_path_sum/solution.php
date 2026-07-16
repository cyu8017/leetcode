// LeetCode 0064 - Minimum Path Sum
// https://leetcode.com/problems/minimum-path-sum/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minPathSum($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($i === 0 && $j === 0) {
                    continue;
                }
                if ($i === 0) {
                    $grid[$i][$j] += $grid[$i][$j - 1];
                } elseif ($j === 0) {
                    $grid[$i][$j] += $grid[$i - 1][$j];
                } else {
                    $grid[$i][$j] += min($grid[$i - 1][$j], $grid[$i][$j - 1]);
                }
            }
        }

        return $grid[$rows - 1][$cols - 1];
    }
}
