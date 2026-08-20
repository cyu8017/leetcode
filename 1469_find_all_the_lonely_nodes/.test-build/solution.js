"use strict";
function getLonelyNodes(root) {
    if (!root)
        return [];
    const result = [], stack = [root];
    while (stack.length) {
        const node = stack.pop();
        if (node.left) {
            if (!node.right)
                result.push(node.left.val);
            stack.push(node.left);
        }
        if (node.right) {
            if (!node.left)
                result.push(node.right.val);
            stack.push(node.right);
        }
    }
    return result;
}
