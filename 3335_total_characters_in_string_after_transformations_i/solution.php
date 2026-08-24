<?php
// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

class Solution {
    function lengthAfterTransformations($s, $t) {
        $mod = 1000000007;
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        for ($step = 0; $step < $t; $step++) {
            $ncnt = array_fill(0, 26, 0);
            for ($i = 0; $i < 25; $i++) $ncnt[$i + 1] = ($ncnt[$i + 1] + $cnt[$i]) % $mod;
            $ncnt[0] = ($ncnt[0] + $cnt[25]) % $mod;
            $ncnt[1] = ($ncnt[1] + $cnt[25]) % $mod;
            $cnt = $ncnt;
        }
        $ans = 0;
        foreach ($cnt as $v) $ans = ($ans + $v) % $mod;
        return $ans;
    }
}
