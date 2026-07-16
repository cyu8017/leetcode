// LeetCode 0361 - Bomb Enemy
// https://leetcode.com/problems/bomb-enemy/

class Solution {
    /**
     * @param String[][] $grid
     * @return Integer
     */
    function maxKilledEnemies($grid) {
        return $this->max_killed_enemies($grid);
    }

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function max_killed_enemies($grid) {
        if ($grid === null || count($grid) === 0 || count($grid[0]) === 0) {
            return 0;
        }

        $rows = count($grid);
        $cols = count($grid[0]);
        $rowHits = array_fill(0, $rows, array_fill(0, $cols, 0));
        $colHits = array_fill(0, $rows, array_fill(0, $cols, 0));

        for ($row = 0; $row < $rows; $row++) {
            $count = 0;
            for ($col = 0; $col < $cols; $col++) {
                if ($grid[$row][$col] === 'W') {
                    $count = 0;
                } elseif ($grid[$row][$col] === 'E') {
                    $count++;
                } else {
                    $rowHits[$row][$col] = $count;
                }
            }

            $count = 0;
            for ($col = $cols - 1; $col >= 0; $col--) {
                if ($grid[$row][$col] === 'W') {
                    $count = 0;
                } elseif ($grid[$row][$col] === 'E') {
                    $count++;
                } else {
                    $rowHits[$row][$col] += $count;
                }
            }
        }

        for ($col = 0; $col < $cols; $col++) {
            $count = 0;
            for ($row = 0; $row < $rows; $row++) {
                if ($grid[$row][$col] === 'W') {
                    $count = 0;
                } elseif ($grid[$row][$col] === 'E') {
                    $count++;
                } else {
                    $colHits[$row][$col] = $count;
                }
            }

            $count = 0;
            for ($row = $rows - 1; $row >= 0; $row--) {
                if ($grid[$row][$col] === 'W') {
                    $count = 0;
                } elseif ($grid[$row][$col] === 'E') {
                    $count++;
                } else {
                    $colHits[$row][$col] += $count;
                }
            }
        }

        $best = 0;
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                $best = max($best, $rowHits[$row][$col] + $colHits[$row][$col]);
            }
        }

        return $best;
    }
}
