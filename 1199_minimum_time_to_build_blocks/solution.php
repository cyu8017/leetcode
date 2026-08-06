<?php
// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

class Solution {
    /**
     * @param Integer[] $blocks
     * @param Integer $split
     * @return Integer
     */
    function minBuildTime($blocks, $split) {
        $heap = new SplMinHeap();
        foreach ($blocks as $b) $heap->insert($b);
        while ($heap->count() > 1) {
            $heap->extract();
            $heap->insert($heap->extract() + $split);
        }
        return $heap->extract();
    }
}
