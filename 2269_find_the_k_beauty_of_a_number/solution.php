<?php
// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution {
    function divisorSubstrings($num, $k) {
        $s = (string)$num;
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i + $k <= $n; $i++) {
            $sub = 0;
            for ($j = 0; $j < $k; $j++) $sub = $sub * 10 + (ord($s[$i + $j]) - 48);
            if ($sub !== 0 && $num % $sub === 0) $ans++;
        }
        return $ans;
    }
}
