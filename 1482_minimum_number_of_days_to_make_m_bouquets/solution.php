<?php
class Solution {
    function minDays($bloomDay, $m, $k) {
        if ($m * $k > count($bloomDay)) return -1;
        $possible = function($day) use ($bloomDay, $m, $k) {
            $bouquets = 0;
            $run = 0;
            foreach ($bloomDay as $x) {
                $run = $x <= $day ? $run + 1 : 0;
                if ($run === $k) {
                    $bouquets++;
                    $run = 0;
                }
            }
            return $bouquets >= $m;
        };
        $lo = min($bloomDay);
        $hi = max($bloomDay);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($possible($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
