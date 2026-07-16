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

export function rob(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null): [number, number] => {
        if (!node) return [0, 0];
        const [leftWith, leftWithout] = dfs(node.left);
        const [rightWith, rightWithout] = dfs(node.right);
        const withRob = node.val + leftWithout + rightWithout;
        const withoutRob = Math.max(leftWith, leftWithout) + Math.max(rightWith, rightWithout);
        return [withRob, withoutRob];
    };

    const [withRob, withoutRob] = dfs(root);
    return Math.max(withRob, withoutRob);
}
