<?php
// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

class Solution {
    /**
     * @param Integer $batchSize
     * @param Integer[] $groups
     * @return Integer
     */
    function maxHappyGroups($batchSize, $groups) {
        $count = array_fill(0, $batchSize, 0);
        foreach ($groups as $size) {
            $count[$size % $batchSize]++;
        }

        $memo = [];

        $dfs = function ($remainder, $state) use (&$dfs, &$memo, $batchSize) {
            $key = $remainder . ':' . implode(',', $state);
            if (isset($memo[$key])) {
                return $memo[$key];
            }

            $best = 0;
            for ($mod = 1; $mod < $batchSize; $mod++) {
                if ($state[$mod] === 0) {
                    continue;
                }
                $state[$mod]--;
                $best = max($best, $dfs(($remainder + $mod) % $batchSize, $state));
                $state[$mod]++;
            }
            if ($remainder === 0) {
                $best++;
            }
            $memo[$key] = $best;
            return $best;
        };

        $ans = $dfs(0, $count);
        if ($count[0] > 0) {
            $ans += $count[0] - 1;
        }
        return $ans;
    }
}
