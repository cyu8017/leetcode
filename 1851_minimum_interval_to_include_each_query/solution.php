<?php
// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

class SizeHeap extends SplMinHeap {
    protected function compare($value1, $value2): int {
        if ($value1[0] !== $value2[0]) {
            return $value2[0] <=> $value1[0];
        }
        return $value2[1] <=> $value1[1];
    }
}

class Solution {
    /**
     * @param Integer[][] $intervals
     * @param Integer[] $queries
     * @return Integer[]
     */
    function minInterval($intervals, $queries) {
        usort($intervals, function ($a, $b) {
            return $a[0] <=> $b[0];
        });

        $indexedQueries = [];
        foreach ($queries as $index => $query) {
            $indexedQueries[] = [$index, $query];
        }
        usort($indexedQueries, function ($a, $b) {
            return $a[1] <=> $b[1];
        });

        $heap = new SizeHeap();
        $answer = array_fill(0, count($queries), -1);
        $intervalIdx = 0;
        $intervalCount = count($intervals);

        foreach ($indexedQueries as [$queryIdx, $query]) {
            while ($intervalIdx < $intervalCount && $intervals[$intervalIdx][0] <= $query) {
                [$left, $right] = $intervals[$intervalIdx];
                $heap->insert([$right - $left + 1, $right]);
                $intervalIdx++;
            }

            while (!$heap->isEmpty() && $heap->top()[1] < $query) {
                $heap->extract();
            }

            if (!$heap->isEmpty()) {
                $answer[$queryIdx] = $heap->top()[0];
            }
        }

        return $answer;
    }
}
