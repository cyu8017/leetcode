<?php
// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

class Solution {
    function recoverOrder($order, $friends) {
        $n = count($order);
        $d = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $d[$order[$i]] = $i;
        usort($friends, function($a, $b) use ($d) { return $d[$a] <=> $d[$b]; });
        return $friends;
    }
}
