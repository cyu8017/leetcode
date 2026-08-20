"use strict";
function goodNodes(root) { const dfs = (node, maximum) => !node ? 0 : (node.val >= maximum ? 1 : 0) + dfs(node.left, Math.max(maximum, node.val)) + dfs(node.right, Math.max(maximum, node.val)); return dfs(root, -Infinity); }
