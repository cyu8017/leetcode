// LeetCode 0314 - Binary Tree Vertical Order Traversal
export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export function verticalOrder(root: TreeNode | null): number[][] {
    if (!root) return [];
    const columns = new Map<number, number[]>();
    const queue: [TreeNode, number][] = [[root, 0]];
    let minCol = 0;
    let maxCol = 0;
    while (queue.length > 0) {
        const [node, column] = queue.shift() as [TreeNode, number];
        minCol = Math.min(minCol, column);
        maxCol = Math.max(maxCol, column);
        if (!columns.has(column)) columns.set(column, []);
        columns.get(column)!.push(node.val);
        if (node.left) queue.push([node.left, column - 1]);
        if (node.right) queue.push([node.right, column + 1]);
    }
    const result: number[][] = [];
    for (let column = minCol; column <= maxCol; column += 1) {
        result.push(columns.get(column) || []);
    }
    return result;
}
