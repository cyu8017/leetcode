<?php
// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

class Solution {
    /**
     * @param String[] $strs
     * @return String[][]
     */
    function groupAnagrams($strs) {
        $groups = [];

        foreach ($strs as $word) {
            $chars = str_split($word);
            sort($chars);
            $key = implode('', $chars);
            if (!isset($groups[$key])) {
                $groups[$key] = [];
            }
            $groups[$key][] = $word;
        }

        $result = [];
        foreach ($groups as $group) {
            sort($group);
            $result[] = $group;
        }

        usort($result, function ($left, $right) use ($strs) {
            return minGroupIndex($strs, $right) <=> minGroupIndex($strs, $left);
        });

        return $result;
    }

    private function minGroupIndex($strs, $group) {
        $min = count($strs);
        foreach ($group as $word) {
            foreach ($strs as $index => $candidate) {
                if ($candidate === $word) {
                    $min = min($min, $index);
                    break;
                }
            }
        }
        return $min;
    }
}
