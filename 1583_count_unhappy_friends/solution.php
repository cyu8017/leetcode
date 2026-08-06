<?php

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $preferences
     * @param Integer[][] $pairs
     * @return Integer
     */
    function unhappyFriends($n, $preferences, $pairs) {
        $rank = [];
        for ($x = 0; $x < $n; $x++) {
            $rank[$x] = [];
            foreach ($preferences[$x] as $i => $friend) {
                $rank[$x][$friend] = $i;
            }
        }
        $partner = [];
        foreach ($pairs as $pair) {
            $partner[$pair[0]] = $pair[1];
            $partner[$pair[1]] = $pair[0];
        }
        $unhappy = 0;
        for ($x = 0; $x < $n; $x++) {
            $y = $partner[$x];
            $limit = $rank[$x][$y];
            for ($i = 0; $i < $limit; $i++) {
                $u = $preferences[$x][$i];
                if ($rank[$u][$x] < $rank[$u][$partner[$u]]) {
                    $unhappy++;
                    break;
                }
            }
        }
        return $unhappy;
    }
}
