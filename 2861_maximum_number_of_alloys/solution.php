<?php
// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

class Solution {
    function maxNumberOfAlloys($n, $k, $budget, $composition, $stock, $cost) {
        $ok = function($machines) use ($n, $composition, $stock, $cost, $budget) {
            foreach ($composition as $comp) {
                $spend = 0;
                for ($i = 0; $i < $n; $i++) {
                    $need = $machines * $comp[$i] - $stock[$i];
                    if ($need > 0) $spend += $need * $cost[$i];
                }
                if ($spend <= $budget) return true;
            }
            return false;
        };
        $lo = 0;
        $hi = 1000000000;
        $ans = 0;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) {
                $ans = $mid;
                $lo = $mid + 1;
            } else $hi = $mid - 1;
        }
        return $ans;
    }
}
