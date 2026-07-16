// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

class Solution {
    /**
     * @param int[][] $grid
     * @return int
     */
    function islandPerimeter($grid) {
        return $this->island_perimeter($grid);
    }

    /**
     * @param int[][] $grid
     * @return int
     */
    function island_perimeter($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $perimeter = 0;

        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($grid[$row][$col] === 0) {
                    continue;
                }
                $perimeter += 4;
                if ($row > 0 && $grid[$row - 1][$col] === 1) {
                    $perimeter -= 2;
                }
                if ($col > 0 && $grid[$row][$col - 1] === 1) {
                    $perimeter -= 2;
                }
            }
        }

        return $perimeter;
    }
}
