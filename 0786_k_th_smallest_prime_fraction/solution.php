<?php
// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer[]
     */
    function kthSmallestPrimeFraction($arr, $k) {
        $n = count($arr);
        $heap = [];
        $push = function($i, $j) use (&$heap, $arr) {
            $heap[] = [$i, $j];
            $idx = count($heap) - 1;
            while ($idx > 0) {
                $p = ($idx - 1) >> 1;
                if ($arr[$heap[$idx][0]] / $arr[$heap[$idx][1]] >= $arr[$heap[$p][0]] / $arr[$heap[$p][1]]) break;
                $tmp = $heap[$idx];
                $heap[$idx] = $heap[$p];
                $heap[$p] = $tmp;
                $idx = $p;
            }
        };
        $pop = function() use (&$heap, $arr) {
            $top = $heap[0];
            $last = array_pop($heap);
            if (count($heap)) {
                $heap[0] = $last;
                $idx = 0;
                while (true) {
                    $smallest = $idx;
                    $l = $idx * 2 + 1;
                    $r = $idx * 2 + 2;
                    if ($l < count($heap) && $arr[$heap[$l][0]] / $arr[$heap[$l][1]] < $arr[$heap[$smallest][0]] / $arr[$heap[$smallest][1]]) $smallest = $l;
                    if ($r < count($heap) && $arr[$heap[$r][0]] / $arr[$heap[$r][1]] < $arr[$heap[$smallest][0]] / $arr[$heap[$smallest][1]]) $smallest = $r;
                    if ($smallest === $idx) break;
                    $tmp = $heap[$idx];
                    $heap[$idx] = $heap[$smallest];
                    $heap[$smallest] = $tmp;
                    $idx = $smallest;
                }
            }
            return $top;
        };
        for ($i = 0; $i < $n - 1; $i++) $push($i, $n - 1);
        for ($t = 0; $t < $k - 1; $t++) {
            [$i, $j] = $pop();
            if ($j - 1 > $i) $push($i, $j - 1);
        }
        [$i, $j] = $pop();
        return [$arr[$i], $arr[$j]];
    }
}
