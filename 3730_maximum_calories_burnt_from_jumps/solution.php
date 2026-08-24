<?php
// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

class Solution {
    function maxCaloriesBurnt($heights) {
        sort($heights);
        $ans = 0;
        $pre = 0;
        $l = 0;
        $r = count($heights) - 1;
        while ($l < $r) {
            $d1 = $heights[$r] - $pre;
            $ans += $d1 * $d1;
            $d2 = $heights[$l] - $heights[$r];
            $ans += $d2 * $d2;
            $pre = $heights[$l];
            $l++;
            $r--;
        }
        $d = $heights[$r] - $pre;
        $ans += $d * $d;
        return $ans;
    }
}
