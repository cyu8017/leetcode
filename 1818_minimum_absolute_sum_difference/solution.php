<?php
// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minAbsoluteSumDiff($nums1, $nums2) {
        $mod = 1000000007;
        $sortedNums1 = $nums1;
        sort($sortedNums1);

        $total = 0;
        foreach ($nums1 as $i => $a) {
            $total += abs($a - $nums2[$i]);
        }

        $bestGain = 0;
        foreach ($nums2 as $i => $target) {
            $current = abs($nums1[$i] - $target);
            $idx = $this->bisectLeft($sortedNums1, $target);
            foreach ([$idx - 1, $idx] as $j) {
                if ($j >= 0 && $j < count($sortedNums1)) {
                    $bestGain = max($bestGain, $current - abs($sortedNums1[$j] - $target));
                }
            }
        }

        return ($total - $bestGain) % $mod;
    }

    /**
     * @param int[] $array
     * @param int $target
     * @return int
     */
    private function bisectLeft($array, $target) {
        $left = 0;
        $right = count($array);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($array[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
