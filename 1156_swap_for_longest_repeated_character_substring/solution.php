<?php
// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

class Solution {
    /**
     * @param String $text
     * @return Integer
     */
    function maxRepOpt1($text) {
        $count = array_count_values(str_split($text));
        $n = strlen($text);
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $text[$j] === $text[$i]) $j++;
            $length = $j - $i;
            $k = $j + 1;
            while ($k < $n && $text[$k] === $text[$i]) $k++;
            $length2 = $j < $n ? $k - $j - 1 : 0;
            $ans = max($ans, min($length + $length2 + 1, $count[$text[$i]]));
            $i = $j;
        }
        return $ans;
    }
}
