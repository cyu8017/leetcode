<?php
// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

class Solution {
    function canAliceWin($a, $b) {
        $i = 0;
        $j = 0;
        $last = chr(0);
        $alice = true;
        while (true) {
            if ($alice) {
                while ($i < count($a) && $a[$i][0] <= $last) $i++;
                if ($i === count($a)) return false;
                $w = $a[$i];
                $last = $w[strlen($w) - 1];
                $i++;
            } else {
                while ($j < count($b) && $b[$j][0] <= $last) $j++;
                if ($j === count($b)) return true;
                $w = $b[$j];
                $last = $w[strlen($w) - 1];
                $j++;
            }
            $alice = !$alice;
        }
    }
}
