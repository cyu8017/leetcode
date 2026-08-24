<?php
// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

class Solution {
    function closestFair($n) {
        for ($x = $n; ; $x++) {
            $s = (string)$x;
            $len = strlen($s);
            if ($len % 2 !== 0) {
                $p = 1;
                for ($i = 0; $i < $len; $i++) $p *= 10;
                return $this->closestFair($p);
            }
            $even = 0;
            $odd = 0;
            for ($i = 0; $i < $len; $i++) {
                if ((ord($s[$i]) - 48) % 2 === 0) $even++;
                else $odd++;
            }
            if ($even === $odd) return $x;
        }
    }
}
