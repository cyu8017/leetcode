const makeNode = (val: any, children: any = []): any => ({ val, children });

function cloneTree(root: any): any {
    if (!root) return null;
    return makeNode(root.val, root.children.map(cloneTree));
}
