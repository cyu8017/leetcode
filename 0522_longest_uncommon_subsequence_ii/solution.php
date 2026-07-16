<?php
// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution {
    /**
     * @param String[] $strs
     * @return Integer
     */
    function findLUSlength($strs) {
        return $this->find_luslength($strs);
    }

    /**
     * @param String[] $strs
     * @return Integer
     */
    function find_luslength($strs) {
        $result = -1;
        foreach ($strs as $i => $candidate) {
            $skip = false;
            foreach ($strs as $j => $other) {
                if ($i !== $j && $this->isSubsequence($candidate, $other)) {
                    $skip = true;
                    break;
                }
            }
            if ($skip) {
                continue;
            }
            $result = max($result, strlen($candidate));
        }
        return $result;
    }

    /**
     * @param String $target
     * @param String $source
     * @return Boolean
     */
    private function isSubsequence($target, $source) {
        $index = 0;
        $length = strlen($target);
        $sourceLength = strlen($source);
        for ($i = 0; $i < $sourceLength; $i++) {
            if ($index < $length && $target[$index] === $source[$i]) {
                $index++;
            }
        }
        return $index === $length;
    }
}
