<?php
// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

class Solution {
    function appealSum($s) {
        $last = array_fill(0, 26, -1);
        $ans = 0;
        $cur = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $cur += $i - $last[$c];
            $last[$c] = $i;
            $ans += $cur;
        }
        return $ans;
    }
}
