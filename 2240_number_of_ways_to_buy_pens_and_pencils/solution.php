<?php
// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution {
    function waysToBuyPensPencils($total, $cost1, $cost2) {
        $ans = 0;
        for ($pens = 0; $pens * $cost1 <= $total; $pens++) {
            $remain = $total - $pens * $cost1;
            $ans += intdiv($remain, $cost2) + 1;
        }
        return $ans;
    }
}
