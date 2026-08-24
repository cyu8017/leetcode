// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

var toArray = function(head) {
    const ans = [];
    while (head !== null) {
        ans.push(head.val);
        head = head.next;
    }
    return ans;
};
