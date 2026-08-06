<?php

class Solution {
    /**
     * @param Integer[] $position
     * @param Integer $m
     * @return Integer
     */
    function maxDistance($position, $m) {
        sort($position);
        $lo = 1;
        $hi = intdiv($position[count($position) - 1] - $position[0], $m - 1);
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $count = 1;
            $last = $position[0];
            $n = count($position);
            for ($i = 1; $i < $n; $i++) {
                if ($position[$i] - $last >= $mid) {
                    $count++;
                    $last = $position[$i];
                }
            }
            if ($count >= $m) {
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $hi;
    }
}
