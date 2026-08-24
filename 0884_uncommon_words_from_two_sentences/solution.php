<?php
// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution {
    function uncommonFromSentences($s1, $s2) {
        $count = [];
        foreach (explode(" ", $s1 . " " . $s2) as $w) {
            if ($w === "") continue;
            $count[$w] = ($count[$w] ?? 0) + 1;
        }
        $ans = [];
        foreach ($count as $k => $v) {
            if ($v === 1) $ans[] = $k;
        }
        return $ans;
    }
}
