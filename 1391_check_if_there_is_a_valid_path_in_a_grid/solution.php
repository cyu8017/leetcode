<?php
class Solution {
    function hasValidPath($grid) {
        $dirs = [
            1 => [[0, -1], [0, 1]],
            2 => [[-1, 0], [1, 0]],
            3 => [[0, -1], [1, 0]],
            4 => [[0, 1], [1, 0]],
            5 => [[0, -1], [-1, 0]],
            6 => [[0, 1], [-1, 0]],
        ];
        $m = count($grid);
        $n = count($grid[0]);
        $seen = ["0,0" => true];
        $st = [[0, 0]];
        while ($st) {
            [$r, $c] = array_pop($st);
            if ($r === $m - 1 && $c === $n - 1) return true;
            foreach ($dirs[$grid[$r][$c]] as [$dr, $dc]) {
                $x = $r + $dr;
                $y = $c + $dc;
                $key = "$x,$y";
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n && !isset($seen[$key])) {
                    $ok = false;
                    foreach ($dirs[$grid[$x][$y]] as [$adr, $adc]) {
                        if ($adr === -$dr && $adc === -$dc) $ok = true;
                    }
                    if ($ok) {
                        $seen[$key] = true;
                        $st[] = [$x, $y];
                    }
                }
            }
        }
        return false;
    }
}
