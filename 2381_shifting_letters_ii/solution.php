<?php
// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

class Solution {
    function shiftingLetters($s, $shifts) {
        $n = strlen($s);
        $diff = array_fill(0, $n + 1, 0);
        foreach ($shifts as $sh) {
            $d = $sh[2] === 0 ? -1 : 1;
            $diff[$sh[0]] += $d;
            $diff[$sh[1] + 1] -= $d;
        }
        $arr = $s;
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = ($cur + $diff[$i]) % 26;
            if ($cur < 0) $cur += 26;
            $arr[$i] = chr(97 + (ord($arr[$i]) - 97 + $cur) % 26);
        }
        return $arr;
    }
}
