<?php
class Solution {
    /**
     * @param String[][] $board
     * @param Integer $rMove
     * @param Integer $cMove
     * @param String $color
     * @return Boolean
     */
    function checkMove($board, $rMove, $cMove, $color) {
        $opp = $color === 'B' ? 'W' : 'B';
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]];
        foreach ($dirs as $d) {
            $dr = $d[0];
            $dc = $d[1];
            $r = $rMove + $dr;
            $c = $cMove + $dc;
            $steps = 0;
            while ($r >= 0 && $r < 8 && $c >= 0 && $c < 8 && $board[$r][$c] === $opp) {
                $r += $dr;
                $c += $dc;
                $steps++;
            }
            if ($steps && $r >= 0 && $r < 8 && $c >= 0 && $c < 8 && $board[$r][$c] === $color) {
                return true;
            }
        }
        return false;
    }
}
