<?php
// LeetCode 2169 - Count Operations to Obtain Zero
// https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution {
    /**
     * @param Integer $num1
     * @param Integer $num2
     * @return Integer
     */
    function countOperations($num1, $num2) {
        $ans = 0;
        while ($num1 > 0 && $num2 > 0) {
            if ($num1 >= $num2) { $ans += intdiv($num1, $num2); $num1 %= $num2; }
            else { $ans += intdiv($num2, $num1); $num2 %= $num1; }
        }
        return $ans;
    }
}
