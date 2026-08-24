<?php
// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDifference($nums) {
        $n = intdiv(count($nums), 3);
        $left = array_fill(0, count($nums), 0);
        $right = array_fill(0, count($nums), 0);
        $hmax = new SplPriorityQueue();
        $hmax->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            $hmax->insert($nums[$i], $nums[$i]);
            $sum += $nums[$i];
        }
        $left[$n - 1] = $sum;
        for ($i = $n; $i < 2 * $n; $i++) {
            $hmax->insert($nums[$i], $nums[$i]);
            $sum += $nums[$i];
            $sum -= $hmax->extract();
            $left[$i] = $sum;
        }
        $hmin = new SplPriorityQueue();
        $hmin->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $sum = 0;
        for ($i = count($nums) - 1; $i >= 2 * $n; $i--) {
            $hmin->insert($nums[$i], -$nums[$i]);
            $sum += $nums[$i];
        }
        $right[2 * $n] = $sum;
        for ($i = 2 * $n - 1; $i >= $n; $i--) {
            $hmin->insert($nums[$i], -$nums[$i]);
            $sum += $nums[$i];
            $sum -= $hmin->extract();
            $right[$i] = $sum;
        }
        $ans = $left[$n - 1] - $right[$n];
        for ($i = $n; $i < 2 * $n; $i++) $ans = min($ans, $left[$i] - $right[$i + 1]);
        return $ans;
    }
}
