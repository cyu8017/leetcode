<?php
// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

class Solution {
    function colorRed($n) {
        $ans = [];
        for ($i = 1; $i <= $n; $i++) $ans[] = [$i, 1];
        for ($i = $n % 2 + 2; $i <= $n; $i += 2) {
            for ($j = 2; $j <= 2 * ($n - $i) + 2; $j++) $ans[] = [$i, $j];
        }
        return $ans;
    }
}
