<?php
// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

class Solution {
    function minCostGoodCaption($caption) {
        $n = strlen($caption);
        if ($n < 3) return "";
        $ans = str_split($caption);
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $ans[$j] === $ans[$i]) $j++;
            if ($j - $i >= 3) { $i = $j; continue; }
            $need = 3 - ($j - $i);
            if ($j + $need <= $n) {
                for ($t = 0; $t < $need; $t++) $ans[$j + $t] = $ans[$i];
                $i = $j + $need;
            } else {
                $ch = "a";
                if ($i > 0) $ch = $ans[$i - 1];
                else if ($j < $n) $ch = $caption[$j];
                for ($t = $i; $t < $n; $t++) $ans[$t] = $ch;
                break;
            }
        }
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $ans[$j] === $ans[$i]) $j++;
            if ($j - $i < 3) return "";
            $i = $j;
        }
        return implode("", $ans);
    }
}
