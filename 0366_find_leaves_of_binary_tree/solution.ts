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

export function findLeaves(root: TreeNode | null): number[][] {
    const layers: number[][] = [];

    const dfs = (node: TreeNode | null): number => {
        if (!node) return -1;
        const height = Math.max(dfs(node.left), dfs(node.right)) + 1;
        if (!layers[height]) layers[height] = [];
        layers[height].push(node.val);
        return height;
    };

    dfs(root);
    return layers;
}
