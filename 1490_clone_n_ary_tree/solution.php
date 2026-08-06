<?php
class Solution {
    function cloneTree($root) {
        if ($root === null) return null;
        $copy = (object)['val' => $root->val, 'children' => []];
        foreach ($root->children as $child) $copy->children[] = $this->cloneTree($child);
        return $copy;
    }
}
