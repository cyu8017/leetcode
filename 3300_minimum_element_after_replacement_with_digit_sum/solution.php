<?php
// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution {
    function minElement($nums) {
        $ans = 1000000000;
        foreach ($nums as $num) {
            $x = $num;
            $s = 0;
            while ($x > 0) {
                $s += $x % 10;
                $x = intdiv($x, 10);
            }
            if ($s < $ans) $ans = $s;
        }
        return $ans;
    }
}
