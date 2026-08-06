<?php
class Solution {
    function getAllElements($root1, $root2) {
        $inorder = function($root) use (&$inorder) {
            if (!$root) return [];
            return array_merge($inorder($root->left), [$root->val], $inorder($root->right));
        };
        $a = $inorder($root1);
        $b = $inorder($root2);
        $answer = [];
        $i = 0;
        $j = 0;
        while ($i < count($a) || $j < count($b)) {
            if ($j === count($b) || ($i < count($a) && $a[$i] <= $b[$j])) $answer[] = $a[$i++];
            else $answer[] = $b[$j++];
        }
        return $answer;
    }
}
