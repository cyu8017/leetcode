<?php
// LeetCode 0382 - Linked List Random Node
// https://leetcode.com/problems/linked-list-random-node/

class ListNode {
    public int $val;
    public ?ListNode $next;

    function __construct(int $val = 0, ?ListNode $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /** @var ListNode[] */
    private array $nodes = [];

    /**
     * @param int[]|ListNode|null $head
     */
    function __construct($head) {
        if (is_array($head)) {
            $head = $this->buildList($head);
        }

        $current = $head;
        while ($current !== null) {
            $this->nodes[] = $current;
            $current = $current->next;
        }
        mt_srand(327);
    }

    /**
     * @return Integer
     */
    function getRandom() {
        return $this->nodes[array_rand($this->nodes)]->val;
    }

    /**
     * @param int[] $values
     * @return ListNode|null
     */
    private function buildList(array $values): ?ListNode {
        if (count($values) === 0) {
            return null;
        }

        $head = new ListNode($values[0]);
        $current = $head;
        for ($index = 1; $index < count($values); $index++) {
            $current->next = new ListNode($values[$index]);
            $current = $current->next;
        }
        return $head;
    }
}
