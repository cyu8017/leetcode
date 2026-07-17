<?php
// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $firstPlayer
     * @param Integer $secondPlayer
     * @return Integer[]
     */
    function earliestAndLatest($n, $firstPlayer, $secondPlayer) {
        $first = $firstPlayer;
        $second = $secondPlayer;
        $memo = [];

        $cartesianProduct = function ($choices) {
            $result = [[]];
            foreach ($choices as $choice) {
                $next = [];
                foreach ($result as $partial) {
                    foreach ($choice as $item) {
                        $next[] = array_merge($partial, [$item]);
                    }
                }
                $result = $next;
            }
            return $result;
        };

        $dfs = null;
        $dfs = function ($players) use (&$dfs, &$memo, $first, $second, $cartesianProduct) {
            $key = implode(',', $players);
            if (isset($memo[$key])) {
                return $memo[$key];
            }

            $count = count($players);
            $firstIndex = array_search($first, $players, true);
            $secondIndex = array_search($second, $players, true);
            if ($firstIndex + $secondIndex === $count - 1) {
                return $memo[$key] = [1, 1];
            }

            $choices = [];
            for ($index = 0; $index < intdiv($count, 2); $index++) {
                $left = $players[$index];
                $right = $players[$count - 1 - $index];
                if ($left === $first || $left === $second) {
                    $choices[] = [$left];
                } elseif ($right === $first || $right === $second) {
                    $choices[] = [$right];
                } else {
                    $choices[] = [$left, $right];
                }
            }
            if ($count % 2) {
                $choices[] = [$players[intdiv($count, 2)]];
            }

            $earliest = PHP_INT_MAX;
            $latest = 0;
            foreach ($cartesianProduct($choices) as $picks) {
                sort($picks);
                [$early, $late] = $dfs($picks);
                $earliest = min($earliest, $early + 1);
                $latest = max($latest, $late + 1);
            }

            return $memo[$key] = [$earliest, $latest];
        };

        $players = range(1, $n);
        return $dfs($players);
    }
}
