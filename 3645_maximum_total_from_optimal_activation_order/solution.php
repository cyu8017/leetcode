<?php
// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

class Solution {
    function maxTotal($value, $limit) {
        $g = [];
        $n = count($value);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($g[$limit[$i]])) $g[$limit[$i]] = [];
            $g[$limit[$i]][] = $value[$i];
        }
        $ans = 0;
        foreach ($g as $lim => $vs) {
            rsort($vs);
            $m = min($lim, count($vs));
            for ($i = 0; $i < $m; $i++) $ans += $vs[$i];
        }
        return $ans;
    }
}
