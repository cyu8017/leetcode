<?php
// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class Solution {
    private function mask($w) {
        $m = 0;
        $len = strlen($w);
        for ($i = 0; $i < $len; $i++) $m |= 1 << (ord($w[$i]) - 97);
        return $m;
    }

    /**
     * @param String[] $startWords
     * @param String[] $targetWords
     * @return Integer
     */
    function wordCount($startWords, $targetWords) {
        $have = [];
        foreach ($startWords as $w) $have[$this->mask($w)] = true;
        $ans = 0;
        foreach ($targetWords as $w) {
            $m = $this->mask($w);
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                if (isset($have[$m ^ (1 << (ord($w[$i]) - 97))])) {
                    $ans++;
                    break;
                }
            }
        }
        return $ans;
    }
}
