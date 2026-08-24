<?php
// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer[] $nums3
     * @return Integer[]
     */
    function twoOutOfThree($nums1, $nums2, $nums3) {
        $s0 = array_flip($nums1);
        $s1 = array_flip($nums2);
        $s2 = array_flip($nums3);
        $ans = [];
        for ($v = 1; $v <= 100; $v++) {
            $c = (isset($s0[$v]) ? 1 : 0) + (isset($s1[$v]) ? 1 : 0) + (isset($s2[$v]) ? 1 : 0);
            if ($c >= 2) $ans[] = $v;
        }
        return $ans;
    }
}
