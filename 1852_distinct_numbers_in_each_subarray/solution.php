<?php
// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function distinctNumbers($nums, $k) {
        $counts = [];
        for ($i = 0; $i < $k; $i++) {
            $counts[$nums[$i]] = ($counts[$nums[$i]] ?? 0) + 1;
        }

        $result = [count($counts)];
        $left = 0;

        for ($right = $k; $right < count($nums); $right++) {
            $counts[$nums[$right]] = ($counts[$nums[$right]] ?? 0) + 1;
            $outgoing = $nums[$left];
            $counts[$outgoing]--;
            if ($counts[$outgoing] === 0) {
                unset($counts[$outgoing]);
            }
            $left++;
            $result[] = count($counts);
        }

        return $result;
    }
}
