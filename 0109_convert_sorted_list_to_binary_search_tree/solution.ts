// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export function sortedListToBST(head: ListNode | null): TreeNode | null {
    const values: number[] = [];
    while (head) {
        values.push(head.val);
        head = head.next;
    }

    function build(left: number, right: number): TreeNode | null {
        if (left > right) {
            return null;
        }
        const mid = Math.floor((left + right + 1) / 2);
        const root = new TreeNode(values[mid]);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }

    return build(0, values.length - 1);
}
