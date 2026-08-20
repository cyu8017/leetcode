function isValidSequence(root: any, arr: any): any {
    const dfs = (node: any, i: any): any => node && node.val === arr[i] && (i === arr.length - 1 ? !node.left && !node.right : dfs(node.left, i + 1) || dfs(node.right, i + 1));
    return Boolean(dfs(root, 0));
}
