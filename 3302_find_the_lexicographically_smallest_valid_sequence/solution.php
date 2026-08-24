<?php
// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

class Solution {
    function canFinish($w1, $w2, $i, $j, $usedSkip, $right) {
        $m = strlen($w2);
        if ($j >= $m) return true;
        if (!$usedSkip) {
            if ($right[$j] >= $i) return true;
            if ($j + 1 <= $m && $right[$j + 1] > $i) return true;
            if ($right[$j] > $i) return true;
            return false;
        }
        return $right[$j] >= $i;
    }

    function validSequence($word1, $word2) {
        $n = strlen($word1);
        $m = strlen($word2);
        $right = array_fill(0, $m + 1, 0);
        $right[$m] = $n;
        $j = $m - 1;
        for ($i = $n - 1; $i >= 0 && $j >= 0; $i--) {
            if ($word1[$i] === $word2[$j]) {
                $right[$j] = $i;
                $j--;
            }
        }
        for (; $j >= 0; $j--) $right[$j] = -1;
        $ans = array_fill(0, $m, 0);
        $usedSkip = false;
        $i = 0;
        for ($j = 0; $j < $m; $j++) {
            $found = false;
            while ($i < $n) {
                if ($word1[$i] === $word2[$j]) {
                    if ($this->canFinish($word1, $word2, $i + 1, $j + 1, $usedSkip, $right)) {
                        $ans[$j] = $i;
                        $i++;
                        $found = true;
                        break;
                    }
                } else if (!$usedSkip) {
                    if ($this->canFinish($word1, $word2, $i + 1, $j + 1, true, $right)) {
                        $ans[$j] = $i;
                        $i++;
                        $usedSkip = true;
                        $found = true;
                        break;
                    }
                }
                $i++;
            }
            if (!$found) return [];
        }
        return $ans;
    }
}
