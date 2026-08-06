<?php
class Solution {
    function minNumberOfFrogs($croakOfFrogs) {
        $order = ["c" => 0, "r" => 1, "o" => 2, "a" => 3, "k" => 4];
        $counts = array_fill(0, 5, 0);
        $active = 0;
        $answer = 0;
        for ($i = 0; $i < strlen($croakOfFrogs); $i++) {
            $char = $croakOfFrogs[$i];
            if (!isset($order[$char])) return -1;
            $idx = $order[$char];
            if ($idx && $counts[$idx - 1] === 0) return -1;
            if ($idx) $counts[$idx - 1]--;
            $counts[$idx]++;
            if ($idx === 0) {
                $active++;
                $answer = max($answer, $active);
            } elseif ($idx === 4) {
                $counts[4]--;
                $active--;
            }
        }
        return $active === 0 ? $answer : -1;
    }
}
