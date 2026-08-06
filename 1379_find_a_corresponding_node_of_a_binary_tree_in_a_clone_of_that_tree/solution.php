<?php
class Solution {
    function getTargetCopy($original, $cloned, $target) {
        $wanted = is_object($target) ? $target->val : $target;
        $stack = [[$original, $cloned]];
        while ($stack) {
            [$a, $b] = array_pop($stack);
            if ($a->val === $wanted) return $b;
            if ($a->left) $stack[] = [$a->left, $b->left];
            if ($a->right) $stack[] = [$a->right, $b->right];
        }
        return null;
    }
}
