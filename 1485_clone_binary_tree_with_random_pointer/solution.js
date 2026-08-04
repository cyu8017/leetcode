var copyRandomBinaryTree = function(root) {
    const copies = new Map();
    const clone = node => {
        if (!node) return null;
        if (!copies.has(node)) {
            const copy = new Node(node.val);
            copies.set(node, copy);
            copy.left = clone(node.left);
            copy.right = clone(node.right);
            copy.random = clone(node.random);
        }
        return copies.get(node);
    };
    return clone(root);
};
