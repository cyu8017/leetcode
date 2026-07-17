<?php
// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

class Solution {
    /**
     * @param Integer[] $packages
     * @param Integer[][] $boxes
     * @return Integer
     */
    function minWastedSpace($packages, $boxes) {
        sort($packages);
        $prefix = [];
        $running = 0;
        foreach ($packages as $package) {
            $running += $package;
            $prefix[] = $running;
        }

        $answer = PHP_INT_MAX;
        foreach ($boxes as $supplier) {
            sort($supplier);
            $start = 0;
            $wasted = 0;

            foreach ($supplier as $box) {
                $end = $this->bisectRight($packages, $box, $start);
                if ($end === $start) {
                    continue;
                }
                $packageSum = $prefix[$end - 1] - ($start > 0 ? $prefix[$start - 1] : 0);
                $wasted += $box * ($end - $start) - $packageSum;
                $start = $end;
            }

            if ($start === count($packages)) {
                $answer = min($answer, $wasted);
            }
        }

        return $answer === PHP_INT_MAX ? -1 : $answer % 1000000007;
    }

    /**
     * @param int[] $arr
     * @param int $target
     * @param int $lo
     * @return int
     */
    private function bisectRight($arr, $target, $lo = 0) {
        $low = $lo;
        $high = count($arr);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] <= $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        return $low;
    }
}
