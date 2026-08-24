<?php
// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution {
    function maxOperations($s) {
        $ans = 0;
        $cnt = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '1') $cnt++;
            else if ($i > 0 && $s[$i - 1] === '1') $ans += $cnt;
        }
        return $ans;
    }
}
