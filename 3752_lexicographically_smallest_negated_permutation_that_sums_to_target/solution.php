<?php
// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

class Solution {
    function lexicographicallySmallest($n, $target) {
        $total = $n * ($n + 1) / 2;
        if ($target < -$total || $target > $total || ($total - $target) % 2 !== 0) return [];
        $remaining = ($total - $target) / 2;
        $negative = array_fill(0, $n + 1, false);
        for ($value = $n; $value >= 1; $value--) {
            if ($value <= $remaining) {
                $negative[$value] = true;
                $remaining -= $value;
            }
        }
        $answer = [];
        for ($value = $n; $value >= 1; $value--) {
            if ($negative[$value]) $answer[] = -$value;
        }
        for ($value = 1; $value <= $n; $value++) {
            if (!$negative[$value]) $answer[] = $value;
        }
        return $answer;
    }
}
