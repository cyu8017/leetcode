// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

class Solution {
    /**
     * @param Integer[][] $rooms
     * @return void
     */
    function wallsAndGates(&$rooms) {
        if ($rooms === null || count($rooms) === 0) {
            return;
        }
        $rows = count($rooms);
        $cols = count($rooms[0]);
        $queue = [];
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($rooms[$row][$col] === 0) {
                    $queue[] = [$row, $col];
                }
            }
        }
        $directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (count($queue) > 0) {
            [$row, $col] = array_shift($queue);
            foreach ($directions as [$dr, $dc]) {
                $nr = $row + $dr;
                $nc = $col + $dc;
                if ($nr < 0 || $nr >= $rows || $nc < 0 || $nc >= $cols) {
                    continue;
                }
                if ($rooms[$nr][$nc] !== 2147483647) {
                    continue;
                }
                $rooms[$nr][$nc] = $rooms[$row][$col] + 1;
                $queue[] = [$nr, $nc];
            }
        }
    }
}
