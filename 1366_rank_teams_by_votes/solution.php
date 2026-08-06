<?php
class Solution {
    function rankTeams($votes) {
        $m = strlen($votes[0]);
        $count = [];
        foreach (str_split($votes[0]) as $c) $count[$c] = array_fill(0, $m, 0);
        foreach ($votes as $v) {
            for ($i = 0; $i < $m; $i++) $count[$v[$i]][$i]++;
        }
        $teams = array_keys($count);
        usort($teams, function($a, $b) use ($count) {
            for ($i = 0; $i < count($count[$a]); $i++) {
                if ($count[$a][$i] !== $count[$b][$i]) return $count[$b][$i] <=> $count[$a][$i];
            }
            return $a <=> $b;
        });
        return implode("", $teams);
    }
}
