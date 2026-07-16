// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

class Solution {
    /**
     * @param Integer[][] $obstacleGrid
     * @return Integer
     */
    function uniquePathsWithObstacles($obstacleGrid) {
        if ($obstacleGrid[0][0] === 1) {
            return 0;
        }

        $rows = count($obstacleGrid);
        $cols = count($obstacleGrid[0]);
        $row = array_fill(0, $cols, 0);
        $row[0] = 1;

        for ($i = 0; $i < $rows; $i++) {
            if ($obstacleGrid[$i][0] === 1) {
                $row[0] = 0;
            }

            for ($j = 1; $j < $cols; $j++) {
                if ($obstacleGrid[$i][$j] === 1) {
                    $row[$j] = 0;
                } else {
                    $row[$j] += $row[$j - 1];
                }
            }
        }

        return $row[$cols - 1];
    }
}
