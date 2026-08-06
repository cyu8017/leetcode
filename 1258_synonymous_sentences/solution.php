<?php
// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

class Solution {
    /**
     * @param String[][] $synonyms
     * @param String $text
     * @return String[]
     */
    function generateSentences($synonyms, $text) {
        $parent = [];
        $find = function ($x) use (&$parent, &$find) {
            if (!isset($parent[$x])) $parent[$x] = $x;
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($synonyms as [$a, $b]) {
            $ra = $find($a); $rb = $find($b);
            $parent[$ra] = $rb;
        }
        $groups = [];
        foreach ($parent as $word => $_) {
            $groups[$find($word)][] = $word;
        }
        foreach ($groups as &$g) sort($g);
        unset($g);
        $words = explode(' ', $text);
        $choices = [];
        foreach ($words as $w) {
            if (isset($parent[$w])) $choices[] = $groups[$find($w)];
            else $choices[] = [$w];
        }
        $result = [];
        $dfs = function ($i, $cur) use (&$dfs, &$result, $choices) {
            if ($i === count($choices)) {
                $result[] = implode(' ', $cur);
                return;
            }
            foreach ($choices[$i] as $w) {
                $cur[] = $w;
                $dfs($i + 1, $cur);
                array_pop($cur);
            }
        };
        $dfs(0, []);
        return $result;
    }
}
