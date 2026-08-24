<?php
// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

class Solution {
    function maxBalancedSubsequenceSum($nums) {
        $NEG = -4000000000000000000;
        $n = count($nums);
        $keys = [];
        for ($i = 0; $i < $n; $i++) $keys[] = $nums[$i] - $i;
        $uniq = array_values(array_unique($keys));
        sort($uniq);
        $bit = array_fill(0, count($uniq) + 2, $NEG);
        $idxOf = function($v) use ($uniq) {
            $lo = 0;
            $hi = count($uniq);
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
        $query = function($i) use (&$bit, $NEG) {
            $best = $NEG;
            for (; $i > 0; $i -= $i & -$i)
                if ($bit[$i] > $best) $best = $bit[$i];
            return $best;
        };
        $ans = $NEG;
        for ($i = 0; $i < $n; $i++) {
            $id = $idxOf($keys[$i]);
            $best = $query($id);
            $cur = $nums[$i];
            if ($best > $NEG / 2) {
                $cand = $best + $nums[$i];
                if ($cand > $cur) $cur = $cand;
            }
            $update($id, $cur);
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
