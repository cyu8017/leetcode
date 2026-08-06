<?php
class Solution {
    function closestDivisors($num) {
        $best = null;
        foreach ([$num + 1, $num + 2] as $x) {
            for ($a = intval(sqrt($x)); $a >= 1; $a--) {
                if ($x % $a === 0) {
                    $pair = [$a, intdiv($x, $a)];
                    if ($best === null || $pair[1] - $pair[0] < $best[1] - $best[0]) $best = $pair;
                    break;
                }
            }
        }
        return $best;
    }
}
