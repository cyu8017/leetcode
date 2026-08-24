<?php
// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

class Solution {
    function openLock($deadends, $target) {
        $dead = [];
        foreach ($deadends as $d) $dead[$d] = true;
        if (isset($dead['0000'])) return -1;
        $q = ['0000'];
        $stepsQ = [0];
        $seen = ['0000' => true];
        while (count($q) > 0) {
            $state = array_shift($q);
            $steps = array_shift($stepsQ);
            if ($state === $target) return $steps;
            $chars = str_split($state);
            for ($i = 0; $i < 4; $i++) {
                $digit = ord($chars[$i]) - 48;
                foreach ([-1, 1] as $delta) {
                    $chars[$i] = (string)(($digit + $delta + 10) % 10);
                    $nxt = implode('', $chars);
                    $chars[$i] = (string)$digit;
                    if (!isset($seen[$nxt]) && !isset($dead[$nxt])) {
                        $seen[$nxt] = true;
                        $q[] = $nxt;
                        $stepsQ[] = $steps + 1;
                    }
                }
            }
        }
        return -1;
    }
}
