<?php
// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

class Solution {
    function isBalanced($num) {
        $even = 0;
        $odd = 0;
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $even += ord($num[$i]) - 48;
            else $odd += ord($num[$i]) - 48;
        }
        return $even === $odd;
    }
}
