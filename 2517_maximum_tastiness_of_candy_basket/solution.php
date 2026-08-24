<?php
// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution {
    function maximumTastiness($price, $k) {
        sort($price);
        $ok = function ($d) use ($price, $k) {
            $cnt = 1;
            $last = $price[0];
            for ($i = 1; $i < count($price); $i++) {
                if ($price[$i] - $last >= $d) {
                    $cnt++;
                    $last = $price[$i];
                    if ($cnt >= $k) return true;
                }
            }
            return false;
        };
        $lo = 0;
        $hi = $price[count($price) - 1] - $price[0];
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
