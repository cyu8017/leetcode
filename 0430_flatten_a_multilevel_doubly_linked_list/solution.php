// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node {
    public $val = 0;
    public $prev = null;
    public $next = null;
    public $child = null;
    function __construct($val = 0, $prev = null, $next = null, $child = null) {
        $this->val = $val;
        $this->prev = $prev;
        $this->next = $next;
        $this->child = $child;
    }
}

class Solution {
    /**
     * @param Node|null $head
     * @return Node|null
     */
    function flatten($head) {
        $current = $head;
        while ($current !== null) {
            if ($current->child !== null) {
                $nextNode = $current->next;
                $childHead = $this->flatten($current->child);
                $current->next = $childHead;
                $childHead->prev = $current;
                $tail = $childHead;
                while ($tail->next !== null) {
                    $tail = $tail->next;
                }
                $tail->next = $nextNode;
                if ($nextNode !== null) {
                    $nextNode->prev = $tail;
                }
                $current->child = null;
            }
            $current = $current->next;
        }
        return $head;
    }
}
