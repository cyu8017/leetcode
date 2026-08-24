<?php
// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

class Solution {
    function reportSpam($message, $bannedWords) {
        $ban = [];
        foreach ($bannedWords as $w) $ban[$w] = true;
        $cnt = 0;
        foreach ($message as $w) {
            if (isset($ban[$w])) {
                $cnt++;
                if ($cnt >= 2) return true;
            }
        }
        return false;
    }
}
