<?php
// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution {
    function maximumLength($s) {
        $n = strlen($s);
        $ans = -1;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i; $j < $n; $j++) {
                if ($s[$j] !== $s[$i]) break;
                $len = $j - $i + 1;
                $cnt = 0;
                for ($k = 0; $k + $len <= $n; $k++) {
                    $ok = true;
                    for ($t = 0; $t < $len; $t++) {
                        if ($s[$k + $t] !== $s[$i + $t]) { $ok = false; break; }
                    }
                    if ($ok) $cnt++;
                }
                if ($cnt >= 3 && $len > $ans) $ans = $len;
            }
        }
        return $ans;
    }
}
