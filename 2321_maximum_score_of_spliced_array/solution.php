<?php
// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

class Solution {
    function maximumsSplicedArray($nums1, $nums2) {
        return max($this->kadane($nums1, $nums2), $this->kadane($nums2, $nums1));
    }

    private function kadane($a, $b) {
        $best = 0;
        $cur = 0;
        $sum = 0;
        $n = count($a);
        for ($i = 0; $i < $n; ++$i) {
            $sum += $a[$i];
            $cur += $b[$i] - $a[$i];
            if ($cur < 0) $cur = 0;
            $best = max($best, $cur);
        }
        return $sum + $best;
    }
}
