<?php
class Solution {
    function findBestValue($arr, $target) {
        $lo = 0;
        $hi = max($arr);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $sum = 0;
            foreach ($arr as $x) $sum += min($x, $mid);
            if ($sum < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        $before = 0;
        $after = 0;
        foreach ($arr as $x) {
            $before += min($x, $lo - 1);
            $after += min($x, $lo);
        }
        return $target - $before <= $after - $target ? $lo - 1 : $lo;
    }
}
