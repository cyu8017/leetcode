<?php
// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

class Solution {
    function maximumCoins($heroes, $monsters, $coins) {
        $n = count($monsters);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($monsters) {
            return $monsters[$a] <=> $monsters[$b];
        });
        $pref = array_fill(0, $n + 1, 0);
        $ms = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $ms[$i] = $monsters[$idx[$i]];
            $pref[$i + 1] = $pref[$i] + $coins[$idx[$i]];
        }
        $ans = [];
        foreach ($heroes as $h) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($ms[$mid] <= $h) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ans[] = $pref[$lo];
        }
        return $ans;
    }
}
