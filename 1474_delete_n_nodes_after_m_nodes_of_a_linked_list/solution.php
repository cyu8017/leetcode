<?php
class Solution {
    function deleteNodes($head, $m, $n) {
        $cur = $head;
        while ($cur) {
            for ($kept = 1; $kept < $m && $cur; $kept++) $cur = $cur->next;
            if (!$cur) break;
            $drop = $cur->next;
            for ($count = 0; $count < $n && $drop; $count++) $drop = $drop->next;
            $cur->next = $drop;
            $cur = $drop;
        }
        return $head;
    }
}
