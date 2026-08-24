<?php
// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

class Solution {
    function compressedString($word) {
        $ans = "";
        $n = strlen($word);
        for ($i = 0; $i < $n; ) {
            $j = $i + 1;
            while ($j < $n && $word[$j] === $word[$i]) $j++;
            $k = $j - $i;
            while ($k > 0) {
                $x = min(9, $k);
                $ans .= (string)$x . $word[$i];
                $k -= $x;
            }
            $i = $j;
        }
        return $ans;
    }
}
