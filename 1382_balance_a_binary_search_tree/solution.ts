// LeetCode 1382: Balance A Binary Search Tree

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

function balanceBST(root: any): any {
    const values: any[] = [];
    const collect = (node: any): any => { if (node) { collect(node.left); values.push(node.val); collect(node.right); } };
    const build = (left: any, right: any): any => {
        if (left > right) return null;
        const mid = Math.floor((left + right) / 2);
        const node = new TreeNode(values[mid]);
        node.left = build(left, mid - 1);
        node.right = build(mid + 1, right);
        return node;
    };
    collect(root);
    return build(0, values.length - 1);
}
