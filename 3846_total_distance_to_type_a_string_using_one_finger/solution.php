<?php
// LeetCode 3846 - Total Distance to Type a String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

class Solution {
    function totalDistance($s) {
        $pos = [];
        $keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'];
        for ($i = 0; $i < 3; $i++) {
            $len = strlen($keys[$i]);
            for ($j = 0; $j < $len; $j++) $pos[$keys[$i][$j]] = [$i, $j];
        }
        $pre = 'a';
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $cur = $s[$i];
            $p1 = $pos[$pre];
            $p2 = $pos[$cur];
            $ans += abs($p1[0] - $p2[0]) + abs($p1[1] - $p2[1]);
            $pre = $cur;
        }
        return $ans;
    }
}
