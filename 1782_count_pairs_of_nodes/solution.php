<?php
// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $queries
     * @return Integer[]
     */
    function countPairs($n, $edges, $queries) {
        $deg = array_fill(0, $n + 1, 0);
        $shared = [];
        foreach ($edges as $edge) {
            $a = min($edge[0], $edge[1]);
            $b = max($edge[0], $edge[1]);
            $deg[$a]++;
            $deg[$b]++;
            $key = $a * 100000 + $b;
            $shared[$key] = ($shared[$key] ?? 0) + 1;
        }
        $sortedDeg = array_slice($deg, 1);
        sort($sortedDeg);
        $ans = [];
        foreach ($queries as $q) {
            $res = 0;
            $left = 0;
            $right = $n - 1;
            while ($left < $right) {
                if ($sortedDeg[$left] + $sortedDeg[$right] > $q) {
                    $res += $right - $left;
                    $right--;
                } else {
                    $left++;
                }
            }
            foreach ($shared as $key => $count) {
                $a = intdiv($key, 100000);
                $b = $key % 100000;
                $sum = $deg[$a] + $deg[$b];
                if ($sum > $q && $q >= $sum - $count) {
                    $res--;
                }
            }
            $ans[] = $res;
        }
        return $ans;
    }
}
