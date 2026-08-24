<?php
// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

class Solution {
    function maxProfit($prices, $profits) {
        $n = count($prices);
        $ans = -1;
        $uniq = array_values(array_unique($prices));
        sort($uniq);
        $m = count($uniq);
        $bit = array_fill(0, $m + 2, -1);
        $idxOf = function($v) use ($uniq, $m) {
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($uniq[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo + 1;
        };
        $update = function($i, $val) use (&$bit) {
            $len = count($bit);
            for (; $i < $len; $i += $i & -$i)
                if ($val > $bit[$i]) $bit[$i] = $val;
        };
        $query = function($i) use (&$bit) {
            $best = -1;
            for (; $i > 0; $i -= $i & -$i)
                if ($bit[$i] > $best) $best = $bit[$i];
            return $best;
        };
        $maxLeft = array_fill(0, $n, -1);
        for ($j = 0; $j < $n; $j++) {
            $id = $idxOf($prices[$j]);
            $maxLeft[$j] = $query($id - 1);
            $update($id, $profits[$j]);
        }
        for ($j = 0; $j < $n; $j++) {
            $bestR = -1;
            for ($k = $j + 1; $k < $n; $k++)
                if ($prices[$k] > $prices[$j] && $profits[$k] > $bestR) $bestR = $profits[$k];
            if ($maxLeft[$j] >= 0 && $bestR >= 0) {
                $cand = $maxLeft[$j] + $profits[$j] + $bestR;
                if ($cand > $ans) $ans = $cand;
            }
        }
        return $ans;
    }
}
