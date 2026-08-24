<?php
// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

class Solution {
    function rearrangeString($s, $x, $y) {
        $arr = str_split($s);
        $i = 0;
        for ($j = 0; $j < count($arr); $j++) {
            if ($arr[$j] == $y) {
                $tmp = $arr[$i];
                $arr[$i] = $arr[$j];
                $arr[$j] = $tmp;
                $i++;
            }
        }
        return implode('', $arr);
    }
}
