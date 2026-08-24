<?php
// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

class Solution {
    function divisibleGame($nums) {
        $candidates = [2 => true];
        foreach ($nums as $value) {
            for ($divisor = 2; $divisor * $divisor <= $value; $divisor++) {
                if ($value % $divisor != 0) continue;
                $candidates[$divisor] = true;
                $candidates[intdiv($value, $divisor)] = true;
            }
            if ($value > 1) $candidates[$value] = true;
        }
        $bestScore = -(1 << 62);
        $bestK = 0;
        foreach ($candidates as $k => $_) {
            $ending = 0;
            $score = 0;
            for ($i = 0; $i < count($nums); $i++) {
                $value = $nums[$i];
                $contribution = -$value;
                if ($value % $k == 0) $contribution = $value;
                if ($i == 0 || $ending + $contribution < $contribution) $ending = $contribution;
                else $ending += $contribution;
                if ($i == 0 || $ending > $score) $score = $ending;
            }
            if ($score > $bestScore || ($score == $bestScore && $k < $bestK)) {
                $bestScore = $score;
                $bestK = $k;
            }
        }
        $mod = 1000000007;
        $answer = (($bestScore % $mod) * $bestK) % $mod;
        if ($answer < 0) $answer += $mod;
        return $answer;
    }
}
