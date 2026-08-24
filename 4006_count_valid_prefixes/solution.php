<?php
// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

class Solution {
    function countValidPrefixes($s) {
        $ans = 0;
        $t = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] == '1') $t++;
            else $t--;
            if ($t >= -1 && $t <= 1) $ans++;
        }
        return $ans;
    }
}
