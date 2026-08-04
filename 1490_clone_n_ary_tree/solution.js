var cloneTree = function(root) {
    if (!root) return null;
    return new Node(root.val, root.children.map(cloneTree));
};
