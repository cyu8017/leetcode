<?php
// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

class WordDistance {
    /** @var array<string, int[]> */
    private array $positions = [];

    /**
     * @param string[] $wordsDict
     */
    function __construct($wordsDict) {
        foreach ($wordsDict as $index => $word) {
            $this->positions[$word][] = $index;
        }
    }

    function shortest($word1, $word2) {
        $left = $this->positions[$word1];
        $right = $this->positions[$word2];
        $i = 0;
        $j = 0;
        $best = PHP_INT_MAX;
        while ($i < count($left) && $j < count($right)) {
            $best = min($best, abs($left[$i] - $right[$j]));
            if ($left[$i] <= $right[$j]) {
                $i++;
            } else {
                $j++;
            }
        }
        return $best;
    }
}
