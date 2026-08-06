<?php
class Solution {
    function matrixBlockSum($mat, $k) {
        $m = count($mat);
        $n = count($mat[0]);
        $prefix = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $prefix[$r + 1][$c + 1] = $mat[$r][$c] + $prefix[$r][$c + 1] + $prefix[$r + 1][$c] - $prefix[$r][$c];
            }
        }
        $answer = array_fill(0, $m, array_fill(0, $n, 0));
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $r1 = max(0, $r - $k);
                $c1 = max(0, $c - $k);
                $r2 = min($m, $r + $k + 1);
                $c2 = min($n, $c + $k + 1);
                $answer[$r][$c] = $prefix[$r2][$c2] - $prefix[$r1][$c2] - $prefix[$r2][$c1] + $prefix[$r1][$c1];
            }
        }
        return $answer;
    }
}
