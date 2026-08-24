<?php
// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

class TopVotedCandidate {
    private $times;
    private $leaders;

    function __construct($persons, $times) {
        $this->times = $times;
        $this->leaders = [];
        $counts = [];
        $leader = -1;
        foreach ($persons as $i => $p) {
            $counts[$p] = ($counts[$p] ?? 0) + 1;
            if ($leader === -1 || $counts[$p] >= $counts[$leader]) $leader = $p;
            $this->leaders[$i] = $leader;
        }
    }

    function q($t) {
        $lo = 0;
        $hi = count($this->times) - 1;
        $i = -1;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->times[$mid] <= $t) {
                $i = $mid;
                $lo = $mid + 1;
            } else $hi = $mid - 1;
        }
        return $this->leaders[$i];
    }
}
