<?php
// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

class Solution {
    function mapWordWeights($words, $weights) {
        $ans = '';
        foreach ($words as $w) {
            $s = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) $s = ($s + $weights[ord($w[$i]) - 97]) % 26;
            $ans .= chr(97 + (25 - $s));
        }
        return $ans;
    }
}
