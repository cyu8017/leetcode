"use strict";
function pseudoPalindromicPaths(root) { const dfs = (node, mask) => { if (!node)
    return 0; mask ^= 1 << node.val; return !node.left && !node.right ? ((mask & (mask - 1)) === 0 ? 1 : 0) : dfs(node.left, mask) + dfs(node.right, mask); }; return dfs(root, 0); }
