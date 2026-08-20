const makeNode = (val: any): any => ({ val, left: null, right: null, random: null });

function copyRandomBinaryTree(root: any): any {
    const copies = new Map();
    const clone = (node: any): any => {
        if (!node) return null;
        if (!copies.has(node)) {
            const copy = makeNode(node.val);
            copies.set(node, copy);
            copy.left = clone(node.left);
            copy.right = clone(node.right);
            copy.random = clone(node.random);
        }
        return copies.get(node);
    };
    return clone(root);
}
