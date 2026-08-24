<?php
// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

class Solution {
    function slidingPuzzle($board) {
        $start = '';
        foreach ($board as $row) foreach ($row as $cell) $start .= (string)$cell;
        $target = '123450';
        $neighbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]];
        $q = [$start];
        $stepsQ = [0];
        $seen = [$start => true];
        while (count($q) > 0) {
            $state = array_shift($q);
            $steps = array_shift($stepsQ);
            if ($state === $target) return $steps;
            $zero = strpos($state, '0');
            foreach ($neighbors[$zero] as $nei) {
                $nxt = str_split($state);
                $tmp = $nxt[$zero];
                $nxt[$zero] = $nxt[$nei];
                $nxt[$nei] = $tmp;
                $ns = implode('', $nxt);
                if (!isset($seen[$ns])) {
                    $seen[$ns] = true;
                    $q[] = $ns;
                    $stepsQ[] = $steps + 1;
                }
            }
        }
        return -1;
    }
}
