<?php
// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

class Solution {
    function solve($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        rsort($freq);
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] === 0) break;
            $ans += $freq[$i] * (intdiv($i, 9) + 1);
        }
        return $ans;
    }
}
