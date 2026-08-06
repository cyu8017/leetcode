<?php
class Solution {
    function maxJumps($arr, $d) {
        $n = count($arr);
        $dp = array_fill(0, $n, 1);
        $order = [];
        for ($i = 0; $i < $n; $i++) $order[] = [$arr[$i], $i];
        usort($order, function($a, $b) { return $a[0] <=> $b[0]; });
        foreach ($order as [, $i]) {
            foreach ([-1, 1] as $step) {
                $j = $i + $step;
                while ($j >= 0 && $j < $n && abs($j - $i) <= $d && $arr[$j] < $arr[$i]) {
                    $dp[$i] = max($dp[$i], 1 + $dp[$j]);
                    $j += $step;
                }
            }
        }
        return max($dp);
    }
}
