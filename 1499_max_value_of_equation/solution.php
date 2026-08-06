<?php
class Solution {
    function findMaxValueOfEquation($points, $k) {
        $q = [];
        $ans = -10 ** 20;
        foreach ($points as [$x, $y]) {
            while ($q && $x - $q[0][0] > $k) array_shift($q);
            if ($q) $ans = max($ans, $x + $y + $q[0][1]);
            $value = $y - $x;
            while ($q && $q[count($q) - 1][1] <= $value) array_pop($q);
            $q[] = [$x, $value];
        }
        return $ans;
    }
}
