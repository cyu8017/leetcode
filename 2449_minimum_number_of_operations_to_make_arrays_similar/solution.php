<?php
// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution {
    function makeSimilar($nums, $target) {
        sort($nums);
        sort($target);
        $oddN = [];
        $evenN = [];
        $oddT = [];
        $evenT = [];
        foreach ($nums as $x) {
            if ($x % 2 === 0) $evenN[] = $x;
            else $oddN[] = $x;
        }
        foreach ($target as $x) {
            if ($x % 2 === 0) $evenT[] = $x;
            else $oddT[] = $x;
        }
        $ans = 0;
        for ($i = 0; $i < count($oddN); $i++) {
            $diff = $oddN[$i] - $oddT[$i];
            if ($diff > 0) $ans += intdiv($diff, 2);
        }
        for ($i = 0; $i < count($evenN); $i++) {
            $diff = $evenN[$i] - $evenT[$i];
            if ($diff > 0) $ans += intdiv($diff, 2);
        }
        return $ans;
    }
}
