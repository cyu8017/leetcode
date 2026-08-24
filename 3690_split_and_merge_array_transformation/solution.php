<?php
// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

class Solution {
    function minSplitMerge($nums1, $nums2) {
        $n = count($nums1);
        $toArr = function($nums) use ($n) {
            $t = array_fill(0, 6, 0);
            for ($i = 0; $i < $n; $i++) $t[$i] = $nums[$i];
            return $t;
        };
        $key = function($a) { return implode(',', $a); };
        $start = $toArr($nums1);
        $target = $toArr($nums2);
        $vis = [];
        $vis[$key($start)] = true;
        $q = [$start];
        for ($ans = 0; ; $ans++) {
            $nq = [];
            foreach ($q as $cur) {
                if ($key($cur) === $key($target)) return $ans;
                for ($l = 0; $l < $n; $l++) {
                    for ($r = $l; $r < $n; $r++) {
                        $remain = [];
                        $sub = [];
                        for ($i = 0; $i < $l; $i++) $remain[] = $cur[$i];
                        for ($i = $r + 1; $i < $n; $i++) $remain[] = $cur[$i];
                        for ($i = $l; $i <= $r; $i++) $sub[] = $cur[$i];
                        $rn = count($remain);
                        for ($pos = 0; $pos <= $rn; $pos++) {
                            $nxtSlice = array_merge(array_slice($remain, 0, $pos), $sub, array_slice($remain, $pos));
                            $nxt = $toArr($nxtSlice);
                            $k = $key($nxt);
                            if (!isset($vis[$k])) {
                                $vis[$k] = true;
                                $nq[] = $nxt;
                            }
                        }
                    }
                }
            }
            $q = $nq;
        }
    }
}
