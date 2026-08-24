<?php
// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution {
    function minimumLines($stockPrices) {
        if (count($stockPrices) <= 1) return 0;
        usort($stockPrices, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 1;
        for ($i = 2; $i < count($stockPrices); $i++) {
            $x0 = $stockPrices[$i - 2][0];
            $y0 = $stockPrices[$i - 2][1];
            $x1 = $stockPrices[$i - 1][0];
            $y1 = $stockPrices[$i - 1][1];
            $x2 = $stockPrices[$i][0];
            $y2 = $stockPrices[$i][1];
            if (($y1 - $y0) * ($x2 - $x1) !== ($y2 - $y1) * ($x1 - $x0)) $ans++;
        }
        return $ans;
    }
}
