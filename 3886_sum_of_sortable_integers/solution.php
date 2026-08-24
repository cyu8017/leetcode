<?php
// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

class Solution {
    function rotationMatches($block, $target) {
        $k = count($block);
        $prefix = array_fill(0, $k, 0);
        for ($i = 1; $i < $k; $i++) {
            $j = $prefix[$i - 1];
            while ($j > 0 && $target[$i] !== $target[$j]) $j = $prefix[$j - 1];
            if ($target[$i] === $target[$j]) $j++;
            $prefix[$i] = $j;
        }
        $matched = 0;
        $lim = 2 * $k - 1;
        for ($i = 0; $i < $lim; $i++) {
            $x = $block[$i % $k];
            while ($matched > 0 && $x !== $target[$matched]) $matched = $prefix[$matched - 1];
            if ($x === $target[$matched]) $matched++;
            if ($matched === $k) return true;
        }
        return false;
    }
    function sumOfSortableIntegers($nums) {
        $n = count($nums);
        $sorted = $nums;
        sort($sorted);
        $divisors = [];
        for ($d = 1; $d * $d <= $n; $d++) {
            if ($n % $d === 0) {
                $divisors[] = $d;
                if ($d * $d !== $n) $divisors[] = intdiv($n, $d);
            }
        }
        $answer = 0;
        foreach ($divisors as $k) {
            $ok = true;
            for ($start = 0; $start < $n; $start += $k) {
                $block = array_slice($nums, $start, $k);
                $target = array_slice($sorted, $start, $k);
                if (!$this->rotationMatches($block, $target)) { $ok = false; break; }
            }
            if ($ok) $answer += $k;
        }
        return $answer;
    }
}
