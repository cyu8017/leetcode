<?php
// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

class Solution {
    function countWordOccurrences($chunks, $queries) {
        $s = implode('', $chunks);
        $n = strlen($s);
        $cnt = [];
        $i = 0;
        while ($i < $n) {
            if ($s[$i] == ' ' || $s[$i] == '-') {
                $i++;
                continue;
            }
            $j = $i;
            while ($j < $n && $s[$j] != ' ' && ($s[$j] != '-' || ($j + 1 < $n && $s[$j + 1] != ' ' && $s[$j + 1] != '-'))) {
                $j++;
            }
            $word = substr($s, $i, $j - $i);
            $cnt[$word] = ($cnt[$word] ?? 0) + 1;
            $i = $j;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($k = 0; $k < count($queries); $k++) {
            $ans[$k] = $cnt[$queries[$k]] ?? 0;
        }
        return $ans;
    }
}
