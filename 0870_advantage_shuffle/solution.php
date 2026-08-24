<?php
// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function advantageCount($nums1, $nums2) {
        $dq = $nums1;
        sort($dq);
        $lo = 0;
        $hi = count($dq) - 1;
        $ans = array_fill(0, count($nums1), 0);
        $indexed = [];
        $n = count($nums2);
        for ($i = 0; $i < $n; $i++) $indexed[] = [$nums2[$i], $i];
        usort($indexed, function($a, $b) { return $b[0] <=> $a[0]; });
        foreach ($indexed as $item) {
            $val = $item[0];
            $i = $item[1];
            if ($dq[$hi] > $val) $ans[$i] = $dq[$hi--];
            else $ans[$i] = $dq[$lo++];
        }
        return $ans;
    }
}
