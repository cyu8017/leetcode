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

export function largestBSTSubtree(root: TreeNode | null): number {
    let best = 0;

    const dfs = (node: TreeNode | null): [boolean, number, number, number] => {
        if (!node) return [true, Number.MAX_SAFE_INTEGER, Number.MIN_SAFE_INTEGER, 0];

        const [leftOk, leftMin, leftMax, leftSize] = dfs(node.left);
        const [rightOk, rightMin, rightMax, rightSize] = dfs(node.right);

        if (leftOk && rightOk && leftMax < node.val && node.val < rightMin) {
            const size = leftSize + rightSize + 1;
            best = Math.max(best, size);
            return [true, Math.min(leftMin, node.val), Math.max(rightMax, node.val), size];
        }

        return [false, 0, 0, 0];
    };

    dfs(root);
    return best;
}
