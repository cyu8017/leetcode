<?php
// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution {
    function findWinners($matches) {
        $lose = [];
        $seen = [];
        foreach ($matches as $m) {
            $seen[$m[0]] = true;
            $seen[$m[1]] = true;
            $lose[$m[1]] = ($lose[$m[1]] ?? 0) + 1;
        }
        $zero = [];
        $one = [];
        foreach ($seen as $p => $_) {
            $L = $lose[$p] ?? 0;
            if ($L === 0) $zero[] = $p;
            else if ($L === 1) $one[] = $p;
        }
        sort($zero);
        sort($one);
        return [$zero, $one];
    }
}
