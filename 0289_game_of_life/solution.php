// LeetCode 0289 - Game of Life
// https://leetcode.com/problems/game-of-life/

class Solution {
    /**
     * @param Integer[][] $board
     * @return void
     */
    function gameOfLife(&$board) {
        $rows = count($board);
        $cols = count($board[0]);
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                $liveNeighbors = 0;
                for ($dr = -1; $dr <= 1; $dr++) {
                    for ($dc = -1; $dc <= 1; $dc++) {
                        if ($dr === 0 && $dc === 0) {
                            continue;
                        }
                        $nr = $row + $dr;
                        $nc = $col + $dc;
                        if ($nr < 0 || $nr >= $rows || $nc < 0 || $nc >= $cols) {
                            continue;
                        }
                        if (($board[$nr][$nc] & 1) === 1) {
                            $liveNeighbors++;
                        }
                    }
                }
                if (($board[$row][$col] & 1) === 1 && ($liveNeighbors === 2 || $liveNeighbors === 3)) {
                    $board[$row][$col] |= 2;
                } elseif (($board[$row][$col] & 1) === 0 && $liveNeighbors === 3) {
                    $board[$row][$col] |= 2;
                }
            }
        }
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                $board[$row][$col] >>= 1;
            }
        }
    }
}
