<?php
// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution {
    function maxChunksToSorted($arr) {
        $chunks = 0;
        $maxSoFar = 0;
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $maxSoFar = max($maxSoFar, $arr[$i]);
            if ($maxSoFar === $i) $chunks++;
        }
        return $chunks;
    }
}
