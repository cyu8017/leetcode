<?php
// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution {
    function smallestRange($nums) {
        $heap = [];
        $push = function($item) use (&$heap) {
            $heap[] = $item;
            $i = count($heap) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($heap[$p][0] <= $heap[$i][0]) break;
                $tmp = $heap[$p]; $heap[$p] = $heap[$i]; $heap[$i] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$heap) {
            $top = $heap[0];
            $last = array_pop($heap);
            if ($heap) {
                $heap[0] = $last;
                $i = 0;
                while (true) {
                    $smallest = $i;
                    $l = $i * 2 + 1;
                    $r = $i * 2 + 2;
                    if ($l < count($heap) && $heap[$l][0] < $heap[$smallest][0]) $smallest = $l;
                    if ($r < count($heap) && $heap[$r][0] < $heap[$smallest][0]) $smallest = $r;
                    if ($smallest === $i) break;
                    $tmp = $heap[$i]; $heap[$i] = $heap[$smallest]; $heap[$smallest] = $tmp;
                    $i = $smallest;
                }
            }
            return $top;
        };
        $currentMax = PHP_INT_MIN;
        for ($i = 0; $i < count($nums); ++$i) {
            $val = $nums[$i][0];
            $push([$val, $i, 0]);
            $currentMax = max($currentMax, $val);
        }
        $bestLeft = $heap[0][0];
        $bestRight = $currentMax;
        while (true) {
            $item = $pop();
            $value = $item[0];
            $listIndex = $item[1];
            $index = $item[2];
            if ($currentMax - $value < $bestRight - $bestLeft) {
                $bestLeft = $value;
                $bestRight = $currentMax;
            }
            if ($index + 1 === count($nums[$listIndex])) break;
            $nxt = $nums[$listIndex][$index + 1];
            $push([$nxt, $listIndex, $index + 1]);
            $currentMax = max($currentMax, $nxt);
        }
        return [$bestLeft, $bestRight];
    }
}
