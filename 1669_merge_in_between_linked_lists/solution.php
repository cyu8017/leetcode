<?php
// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

class Solution {
    function mergeInBetween($list1, $a, $b, $list2) {
        $pre = $list1;
        for ($i = 0; $i < $a - 1; $i++) $pre = $pre->next;
        $post = $pre;
        for ($i = 0; $i < $b - $a + 2; $i++) $post = $post->next;
        $pre->next = $list2;
        while ($pre->next !== null) $pre = $pre->next;
        $pre->next = $post;
        return $list1;
    }
}
