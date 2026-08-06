<?php
// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

class Solution {
    /**
     * @param Integer[] $status
     * @param Integer[] $candies
     * @param Integer[][] $keys
     * @param Integer[][] $containedBoxes
     * @param Integer[] $initialBoxes
     * @return Integer
     */
    function maxCandies($status, $candies, $keys, $containedBoxes, $initialBoxes) {
        $owned = [];
        foreach ($initialBoxes as $box) $owned[$box] = true;
        $opened = [];
        $queue = [];
        foreach ($initialBoxes as $box) {
            if ($status[$box]) $queue[] = $box;
        }
        $total = 0;
        $head = 0;
        while ($head < count($queue)) {
            $box = $queue[$head++];
            if (isset($opened[$box]) || !$status[$box]) continue;
            $opened[$box] = true;
            $total += $candies[$box];
            foreach ($keys[$box] as $key) {
                $status[$key] = 1;
                if (isset($owned[$key]) && !isset($opened[$key])) $queue[] = $key;
            }
            foreach ($containedBoxes[$box] as $child) {
                $owned[$child] = true;
                if ($status[$child] && !isset($opened[$child])) $queue[] = $child;
            }
        }
        return $total;
    }
}
