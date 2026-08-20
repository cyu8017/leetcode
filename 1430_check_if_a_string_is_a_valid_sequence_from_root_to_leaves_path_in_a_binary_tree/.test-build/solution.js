"use strict";
function isValidSequence(root, arr) {
    const dfs = (node, i) => node && node.val === arr[i] && (i === arr.length - 1 ? !node.left && !node.right : dfs(node.left, i + 1) || dfs(node.right, i + 1));
    return Boolean(dfs(root, 0));
}
