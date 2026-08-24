<?php
// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution {
    function minimumLength($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = 0;
        foreach ($cnt as $x) {
            if ($x > 0) $ans += ($x & 1) !== 0 ? 1 : 2;
        }
        return $ans;
    }
}
