<?php
// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution {
    function getSmallestString($s) {
        $arr = str_split($s);
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            $a = $arr[$i - 1];
            $b = $arr[$i];
            if ($a > $b && (ord($a) % 2) === (ord($b) % 2)) {
                $arr[$i - 1] = $b;
                $arr[$i] = $a;
                return implode('', $arr);
            }
        }
        return $s;
    }
}
