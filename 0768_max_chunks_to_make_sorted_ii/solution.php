<?php
// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

class Solution {
    function maxChunksToSorted($arr) {
        $n = count($arr);
        $maxLeft = array_fill(0, $n, 0);
        $minRight = array_fill(0, $n, 0);
        $maxLeft[0] = $arr[0];
        for ($i = 1; $i < $n; $i++) $maxLeft[$i] = max($maxLeft[$i - 1], $arr[$i]);
        $minRight[$n - 1] = $arr[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $minRight[$i] = min($minRight[$i + 1], $arr[$i]);
        $chunks = 1;
        for ($i = 0; $i < $n - 1; $i++) if ($maxLeft[$i] <= $minRight[$i + 1]) $chunks++;
        return $chunks;
    }
}
