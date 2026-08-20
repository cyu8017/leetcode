"use strict";
const makeNode = (val, children = []) => ({ val, children });
function cloneTree(root) {
    if (!root)
        return null;
    return makeNode(root.val, root.children.map(cloneTree));
}
