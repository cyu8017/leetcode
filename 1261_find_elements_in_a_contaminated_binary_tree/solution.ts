// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function listToTree(values: any): any {
    if (!values || values.length === 0) return null;
    const root = { val: values[0], left: null, right: null };
    const queue = [root];
    let i = 1;
    while (queue.length > 0 && i < values.length) {
        const node = queue.shift();
        if (i < values.length && values[i] !== null && values[i] !== undefined) {
            node.left = { val: values[i], left: null, right: null };
            queue.push(node.left);
        }
        i += 1;
        if (i < values.length && values[i] !== null && values[i] !== undefined) {
            node.right = { val: values[i], left: null, right: null };
            queue.push(node.right);
        }
        i += 1;
    }
    return root;
}

class FindElements {
    values: any;

    constructor(root: TreeNode) {
        this.values = new Set();
        if (Array.isArray(root)) {
            root = listToTree(root);
        }
        const recover = (node, value) => {
            if (!node) return;
            node.val = value;
            this.values.add(value);
            recover(node.left, 2 * value + 1);
            recover(node.right, 2 * value + 2);
        };
        recover(root, 0);
    }

    find(target: number): boolean {
        return this.values.has(target);
    }
}
