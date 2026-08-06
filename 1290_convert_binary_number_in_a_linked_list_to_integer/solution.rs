// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

impl Solution {
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        let mut value = 0;
        let mut cur = head;
        while let Some(node) = cur {
            value = value * 2 + node.val;
            cur = node.next;
        }
        value
    }
}
