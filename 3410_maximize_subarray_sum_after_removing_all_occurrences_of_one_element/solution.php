<?php
// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

class Solution {
    private function kadane($a) {
        $best = PHP_INT_MIN;
        $cur = 0;
        foreach ($a as $x) {
            $cur += $x;
            if ($cur > $best) $best = $cur;
            if ($cur < 0) $cur = 0;
        }
        $allNeg = true;
        $mx = $a[0];
        foreach ($a as $x) {
            if ($x > $mx) $mx = $x;
            if ($x >= 0) $allNeg = false;
        }
        if ($allNeg) return $mx;
        return $best;
    }

    function maxSubarraySum($nums) {
        $ans = $this->kadane($nums);
        $uniq = [];
        foreach ($nums as $x) if ($x < 0) $uniq[$x] = true;
        foreach ($uniq as $v => $_) {
            $b = [];
            foreach ($nums as $x) if ($x !== $v) $b[] = $x;
            if (count($b) === 0) continue;
            $cand = $this->kadane($b);
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
