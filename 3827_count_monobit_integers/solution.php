<?php
// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

class Solution {
    function countMonobit($n) {
        $ans = 1;
        for ($i = 1, $x = 1; $x <= $n; $i++) {
            $ans++;
            $x += (1 << $i);
        }
        return $ans;
    }
}
