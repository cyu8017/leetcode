<?php
// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

class Solution {
    function sortArray($nums) {
        $solveOne = function ($startZero) use ($nums) {
            $n = count($nums);
            $arr = $nums;
            $pos = [];
            for ($i = 0; $i < $n; $i++) $pos[$arr[$i]] = $i;
            $ops = 0;
            while (true) {
                $empty = $pos[0];
                $should = $startZero ? $empty : ($empty === $n - 1 ? 0 : $empty + 1);
                if ($arr[$empty] === $should) {
                    $found = -1;
                    for ($i = 0; $i < $n; $i++) {
                        $want = $startZero ? $i : ($i === $n - 1 ? 0 : $i + 1);
                        if ($arr[$i] !== $want) { $found = $i; break; }
                    }
                    if ($found === -1) return $ops;
                    $v = $arr[$found];
                    $arr[$empty] = $arr[$found];
                    $arr[$found] = 0;
                    $pos[0] = $found;
                    $pos[$v] = $empty;
                    $ops++;
                    continue;
                }
                $j = $pos[$should];
                $vv = $arr[$j];
                $arr[$empty] = $arr[$j];
                $arr[$j] = 0;
                $pos[0] = $j;
                $pos[$vv] = $empty;
                $ops++;
            }
        };
        return min($solveOne(true), $solveOne(false));
    }
}
