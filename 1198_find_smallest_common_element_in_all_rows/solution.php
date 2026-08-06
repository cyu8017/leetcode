<?php
// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function smallestCommonElement($mat) {
        $common = array_flip($mat[0]);
        for ($r = 1; $r < count($mat); $r++) {
            $row = array_flip($mat[$r]);
            $common = array_intersect_key($common, $row);
            if (empty($common)) return -1;
        }
        return min(array_keys($common));
    }
}
