<?php
class Solution {
    function minSumOfLengths($arr, $target) {
        $inf = 1000000000;
        $left = 0;
        $total = 0;
        $best = $inf;
        $ans = $inf;
        $shortest = array_fill(0, count($arr), $inf);
        foreach ($arr as $right => $x) {
            $total += $x;
            while ($total > $target) {
                $total -= $arr[$left];
                $left++;
            }
            if ($total === $target) {
                $length = $right - $left + 1;
                if ($left) $ans = min($ans, $length + $shortest[$left - 1]);
                $best = min($best, $length);
            }
            $shortest[$right] = $best;
        }
        return $ans === $inf ? -1 : $ans;
    }
}
