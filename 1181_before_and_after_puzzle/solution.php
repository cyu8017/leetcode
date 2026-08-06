<?php
// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

class Solution {
    /**
     * @param String[] $phrases
     * @return String[]
     */
    function beforeAndAfterPuzzles($phrases) {
        $split = array_map(fn($p) => explode(' ', $p), $phrases);
        $result = [];
        $m = count($split);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if ($i === $j) continue;
                if ($split[$i][count($split[$i]) - 1] === $split[$j][0]) {
                    $merged = array_merge($split[$i], array_slice($split[$j], 1));
                    $result[implode(' ', $merged)] = true;
                }
            }
        }
        $ans = array_keys($result);
        sort($ans);
        return $ans;
    }
}
