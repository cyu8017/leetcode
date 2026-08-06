<?php
class Solution {
    function luckyNumbers($matrix) {
        $mins = [];
        foreach ($matrix as $r) $mins[min($r)] = true;
        $cols = count($matrix[0]);
        $maxs = [];
        for ($c = 0; $c < $cols; $c++) {
            $mx = $matrix[0][$c];
            for ($r = 1; $r < count($matrix); $r++) $mx = max($mx, $matrix[$r][$c]);
            $maxs[$mx] = true;
        }
        $answer = [];
        foreach ($mins as $v => $_) if (isset($maxs[$v])) $answer[] = $v;
        return $answer;
    }
}
