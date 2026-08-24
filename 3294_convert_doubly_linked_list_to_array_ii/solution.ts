// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

export function toArray(node: any): any {
    while (node !== null && node.prev !== null) node = node.prev;
    const ans = [];
    while (node !== null) {
        ans.push(node.val);
        node = node.next;
    }
    return ans;
}
