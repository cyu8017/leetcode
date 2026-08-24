<?php
// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function majorityElement($nums) {
        $candidate1 = null;
        $candidate2 = null;
        $count1 = 0;
        $count2 = 0;

        foreach ($nums as $num) {
            if ($num === $candidate1) {
                $count1++;
            } elseif ($num === $candidate2) {
                $count2++;
            } elseif ($count1 === 0) {
                $candidate1 = $num;
                $count1 = 1;
            } elseif ($count2 === 0) {
                $candidate2 = $num;
                $count2 = 1;
            } else {
                $count1--;
                $count2--;
            }
        }

        $count1 = 0;
        $count2 = 0;
        foreach ($nums as $num) {
            if ($num === $candidate1) {
                $count1++;
            } elseif ($num === $candidate2) {
                $count2++;
            }
        }

        $threshold = intdiv(count($nums), 3);
        $result = [];
        if ($count1 > $threshold) {
            $result[] = $candidate1;
        }
        if ($candidate2 !== $candidate1 && $count2 > $threshold) {
            $result[] = $candidate2;
        }
        return $result;
    }
}
