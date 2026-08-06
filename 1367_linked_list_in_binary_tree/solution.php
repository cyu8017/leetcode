<?php
class Solution {
    function isSubPath($head, $root) {
        $match = function($a, $b) use (&$match) {
            return !$a || ($b && $a->val === $b->val && ($match($a->next, $b->left) || $match($a->next, $b->right)));
        };
        return $root && ($match($head, $root) || $this->isSubPath($head, $root->left) || $this->isSubPath($head, $root->right));
    }
}
