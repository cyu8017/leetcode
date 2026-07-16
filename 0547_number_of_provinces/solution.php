<?php
// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

class Solution {
    /**
     * @param Integer[][] $isConnected
     * @return Integer
     */
    function findCircleNum($isConnected) {
        return $this->find_circle_num($isConnected);
    }

    /**
     * @param Integer[][] $isConnected
     * @return Integer
     */
    function find_circle_num($isConnected) {
        $n = count($isConnected);
        $parent = range(0, $n - 1);

        $find = function ($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };

        $union = function ($a, $b) use (&$parent, $find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) {
                $parent[$rb] = $ra;
            }
        };

        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($isConnected[$i][$j] !== 0) {
                    $union($i, $j);
                }
            }
        }

        $count = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($find($i) === $i) {
                $count++;
            }
        }
        return $count;
    }
}
