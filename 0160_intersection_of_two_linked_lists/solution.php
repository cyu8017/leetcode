// LeetCode 0160 - Intersection of Two Linked Lists
// https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode {
    public int $val;
    public ?ListNode $next;

    function __construct(int $val = 0, ?ListNode $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function getIntersectionNode(?ListNode $headA, ?ListNode $headB): ?ListNode {
        $a = $headA;
        $b = $headB;
        while ($a !== $b) {
            $a = $a !== null ? $a->next : $headB;
            $b = $b !== null ? $b->next : $headA;
        }
        return $a;
    }
}