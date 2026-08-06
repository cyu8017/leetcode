<?php
class Solution {
    function deepestLeavesSum($root) {
        $level = [$root];
        $answer = 0;
        while ($level) {
            $answer = 0;
            $next = [];
            foreach ($level as $node) {
                $answer += $node->val;
                if ($node->left) $next[] = $node->left;
                if ($node->right) $next[] = $node->right;
            }
            $level = $next;
        }
        return $answer;
    }
}
