<?php
// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[] $pre
     * @return Integer
     */
    function sortArray($nums, $pre) {
        $n = count($nums);
        $start = implode(',', $nums);
        $target = implode(',', range(0, $n - 1));
        if ($start === $target) {
            return 0;
        }

        $lengths = array_values(array_unique(array_filter($pre, function ($i) use ($n) {
            return $i >= 2 && $i <= $n;
        })));
        sort($lengths);

        $visited = [$start => true];
        $queue = [$nums];
        $steps = 0;

        while ($queue) {
            $steps++;
            $nextQueue = [];
            foreach ($queue as $cur) {
                foreach ($lengths as $i) {
                    $nxt = $cur;
                    for ($l = 0, $r = $i - 1; $l < $r; $l++, $r--) {
                        $tmp = $nxt[$l];
                        $nxt[$l] = $nxt[$r];
                        $nxt[$r] = $tmp;
                    }
                    $key = implode(',', $nxt);
                    if ($key === $target) {
                        return $steps;
                    }
                    if (!isset($visited[$key])) {
                        $visited[$key] = true;
                        $nextQueue[] = $nxt;
                    }
                }
            }
            $queue = $nextQueue;
        }
        return -1;
    }
}
