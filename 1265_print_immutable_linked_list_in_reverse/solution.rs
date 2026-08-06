// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

trait ImmutableListNode {
    fn get_next(&self) -> Option<&dyn ImmutableListNode>;
    fn print_value(&self);
}

impl Solution {
    pub fn print_linked_list_in_reverse(head: Option<&dyn ImmutableListNode>) {
        if let Some(node) = head {
            Self::print_linked_list_in_reverse(node.get_next());
            node.print_value();
        }
    }
}
