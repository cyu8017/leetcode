<?php
// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

class Solution {
    function countSpecialNumbers($n) {
        $s = strval($n);
        $m = strlen($s);
        $ans = 0;
        $perm = 9;
        for ($i = 1; $i < $m; $i++) {
            $ans += $perm;
            $perm *= (10 - $i);
        }
        $used = array_fill(0, 10, false);
        for ($i = 0; $i < $m; $i++) {
            $start = $i === 0 ? 1 : 0;
            $digit = ord($s[$i]) - 48;
            for ($d = $start; $d < $digit; $d++) {
                if ($used[$d]) continue;
                $rem = 10 - ($i + 1);
                $ways = 1;
                for ($j = $i + 1; $j < $m; $j++) {
                    $ways *= $rem;
                    $rem--;
                }
                $ans += $ways;
            }
            if ($used[$digit]) return $ans;
            $used[$digit] = true;
        }
        return $ans + 1;
    }
}
