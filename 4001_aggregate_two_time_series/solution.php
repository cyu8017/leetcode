<?php
// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

class Solution {
    function aggregateTimeSeries($series1, $series2) {
        $m = count($series1);
        $n = count($series2);
        $i = 0;
        $j = 0;
        $ans = [];
        while ($i < $m && $j < $n) {
            $t1 = $series1[$i][0];
            $v1 = $series1[$i][1];
            $t2 = $series2[$j][0];
            $v2 = $series2[$j][1];
            if ($t1 === $t2) {
                $ans[] = [$t1, $v1 + $v2];
                $i++;
                $j++;
            } else if ($t1 < $t2) {
                $ans[] = [$t1, $v1 + $v2];
                $i++;
            } else {
                $ans[] = [$t2, $v1 + $v2];
                $j++;
            }
        }
        while ($i < $m) {
            $ans[] = [$series1[$i][0], $series1[$i][1]];
            $i++;
        }
        while ($j < $n) {
            $ans[] = [$series2[$j][0], $series2[$j][1]];
            $j++;
        }
        return $ans;
    }
}
