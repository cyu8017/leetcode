<?php
// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function countPairs($nums1, $nums2) {
        $diff = [];
        foreach ($nums1 as $index => $value) {
            $diff[] = $value - $nums2[$index];
        }
        sort($diff);

        $answer = 0;
        $n = count($diff);
        for ($i = 0; $i < $n; $i++) {
            $target = -$diff[$i];
            $answer += $n - $this->bisectRight($diff, $target, $i + 1);
        }
        return $answer;
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
