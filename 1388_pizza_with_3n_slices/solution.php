<?php
class Solution {
    function maxSizeSlices($slices) {
        $k = intdiv(count($slices), 3);
        $line = function($a) use ($k) {
            $n = count($a);
            $dp = array_fill(0, $n + 2, array_fill(0, $k + 1, 0));
            for ($i = 0; $i < $n; $i++) {
                for ($j = 1; $j <= $k; $j++) {
                    $dp[$i + 2][$j] = max($dp[$i + 1][$j], $dp[$i][$j - 1] + $a[$i]);
                }
            }
            return $dp[$n + 1][$k];
        };
        return max($line(array_slice($slices, 0, -1)), $line(array_slice($slices, 1)));
    }
}
