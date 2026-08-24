<?php
// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

class Solution {
    function minimumCost($nums, $k) {
        $mod = 1000000007;
        $cnt = 0;
        $cur = $k;
        foreach ($nums as $x0) {
            $x = $x0;
            $diff = $x - $cur;
            if ($diff > 0) {
                $m = intdiv($diff + $k - 1, $k);
                $cur += $m * $k;
                $cnt += $m;
            }
            $cur -= $x;
        }
        $cnt %= $mod;
        return intdiv(($cnt + 1) * $cnt, 2) % $mod;
    }
}
