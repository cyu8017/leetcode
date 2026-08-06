<?php
// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution {
    /**
     * @param String[] $folder
     * @return String[]
     */
    function removeSubfolders($folder) {
        sort($folder);
        $answer = [];
        foreach ($folder as $path) {
            if (empty($answer) || !str_starts_with($path, end($answer) . '/')) {
                $answer[] = $path;
            }
        }
        return $answer;
    }
}
