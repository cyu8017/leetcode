<?php
// LeetCode 0315 - Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function countSmaller($nums) {
        $sortedNums = [];
        $result = [];
        for ($index = count($nums) - 1; $index >= 0; $index--) {
            $num = $nums[$index];
            $insertIndex = $this->bisectLeft($sortedNums, $num);
            $result[] = $insertIndex;
            array_splice($sortedNums, $insertIndex, 0, [$num]);
        }
        return array_reverse($result);
    }

    /**
     * @param Integer[] $arr
     * @param Integer $num
     * @return Integer
     */
    private function bisectLeft($arr, $num) {
        $left = 0;
        $right = count($arr);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($arr[$mid] < $num) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
