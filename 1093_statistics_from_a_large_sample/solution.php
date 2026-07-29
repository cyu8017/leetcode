<?php
// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution {
    /**
     * @param Integer[] $count
     * @return Float[]
     */
    function sampleStats($count) {
        $total = array_sum($count);
        $minimum = 0;
        for ($i = 0; $i < 256; $i++) {
            if ($count[$i]) {
                $minimum = $i;
                break;
            }
        }
        $maximum = 0;
        for ($i = 255; $i >= 0; $i--) {
            if ($count[$i]) {
                $maximum = $i;
                break;
            }
        }
        $meanSum = 0;
        $mode = 0;
        $modeCount = -1;
        for ($i = 0; $i < 256; $i++) {
            $meanSum += $i * $count[$i];
            if ($count[$i] > $modeCount) {
                $modeCount = $count[$i];
                $mode = $i;
            }
        }
        $mean = $meanSum / $total;
        $mid1 = intdiv($total + 1, 2);
        $mid2 = intdiv($total + 2, 2);
        $seen = 0;
        $first = null;
        $second = null;
        for ($i = 0; $i < 256; $i++) {
            $seen += $count[$i];
            if ($first === null && $seen >= $mid1) {
                $first = $i;
            }
            if ($second === null && $seen >= $mid2) {
                $second = $i;
                break;
            }
        }
        $median = ($first + $second) / 2.0;
        return [(float)$minimum, (float)$maximum, (float)$mean, (float)$median, (float)$mode];
    }
}
