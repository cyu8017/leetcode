<?php
// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

class Solution {
    function countKeyChanges($s) {
        $s = strtolower($s);
        $ans = 0;
        for ($i = 1; $i < strlen($s); $i++) {
            if ($s[$i] !== $s[$i - 1]) $ans++;
        }
        return $ans;
    }
}
