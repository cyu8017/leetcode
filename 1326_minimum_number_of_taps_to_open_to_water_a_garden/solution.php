<?php
class Solution {
    function minTaps($n, $ranges) {
        $farthest = array_fill(0, $n + 1, 0);
        foreach ($ranges as $center => $radius) {
            $left = max(0, $center - $radius);
            $right = min($n, $center + $radius);
            $farthest[$left] = max($farthest[$left], $right);
        }
        $taps = 0;
        $end = 0;
        $reach = 0;
        for ($position = 0; $position < $n; $position++) {
            $reach = max($reach, $farthest[$position]);
            if ($position === $end) {
                if ($reach <= $position) return -1;
                $taps++;
                $end = $reach;
            }
        }
        return $taps;
    }
}
