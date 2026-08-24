<?php
// LeetCode 0351 - Android Unlock Patterns
// https://leetcode.com/problems/android-unlock-patterns/

class Solution {
    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function numberOfPatterns($m, $n) {
        return $this->number_of_patterns($m, $n);
    }

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function number_of_patterns($m, $n) {
        $jumps = [
            '0,2' => 1, '2,0' => 1,
            '0,6' => 3, '6,0' => 3,
            '0,8' => 4, '8,0' => 4,
            '2,8' => 5, '8,2' => 5,
            '2,6' => 7, '6,2' => 7,
            '6,8' => 7, '8,6' => 7,
            '1,7' => 8, '7,1' => 8,
            '3,7' => 6, '7,3' => 6,
            '1,5' => 4, '5,1' => 4,
            '3,5' => 5, '5,3' => 5,
            '1,3' => 2, '3,1' => 2,
            '4,5' => 5, '5,4' => 5,
            '4,7' => 8, '7,4' => 8,
            '4,3' => 5, '3,4' => 5,
            '4,1' => 2, '1,4' => 2,
            '4,6' => 7, '6,4' => 7,
            '4,8' => 6, '8,4' => 6,
            '4,0' => 2, '0,4' => 2,
            '4,2' => 6, '2,4' => 6,
        ];

        $isValid = function ($visited, $last, $nextCell) use ($jumps) {
            if ($visited & (1 << $nextCell)) {
                return false;
            }

            $key = $last . ',' . $nextCell;
            if (array_key_exists($key, $jumps)) {
                return !($visited & (1 << $jumps[$key]));
            }

            return abs(intdiv($last, 3) - intdiv($nextCell, 3)) <= 1
                && abs(($last % 3) - ($nextCell % 3)) <= 1;
        };

        $dfs = function ($visited, $last, $length) use (&$dfs, $m, $n, $isValid) {
            if ($length > $n) {
                return 0;
            }

            $count = ($m <= $length && $length <= $n) ? 1 : 0;
            for ($nextCell = 0; $nextCell < 9; $nextCell++) {
                if ($isValid($visited, $last, $nextCell)) {
                    $count += $dfs($visited | (1 << $nextCell), $nextCell, $length + 1);
                }
            }

            return $count;
        };

        return $dfs(1 << 0, 0, 1) * 4
            + $dfs(1 << 1, 1, 1) * 4
            + $dfs(1 << 4, 4, 1);
    }
}
