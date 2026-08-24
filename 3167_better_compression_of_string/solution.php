<?php
// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

class Solution {
    function betterCompression($compressed) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($compressed);
        for ($i = 0; $i < $n; ) {
            $c = $compressed[$i];
            $j = $i + 1;
            $x = 0;
            while ($j < $n) {
                $d = $compressed[$j];
                if ($d < "0" || $d > "9") break;
                $x = $x * 10 + (ord($d) - 48);
                $j++;
            }
            $cnt[ord($c) - 97] += $x;
            $i = $j;
        }
        $ans = "";
        for ($c = 0; $c < 26; $c++) {
            if ($cnt[$c] > 0) $ans .= chr(97 + $c) . (string)$cnt[$c];
        }
        return $ans;
    }
}
