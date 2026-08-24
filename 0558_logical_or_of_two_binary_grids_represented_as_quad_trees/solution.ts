// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

class Node {
    val: boolean;
    isLeaf: boolean;
    topLeft: Node | null;
    topRight: Node | null;
    bottomLeft: Node | null;
    bottomRight: Node | null;
    constructor(val?: boolean, isLeaf?: boolean, topLeft?: Node | null, topRight?: Node | null, bottomLeft?: Node | null, bottomRight?: Node | null) {
        this.val = val ?? false;
        this.isLeaf = isLeaf ?? false;
        this.topLeft = topLeft ?? null;
        this.topRight = topRight ?? null;
        this.bottomLeft = bottomLeft ?? null;
        this.bottomRight = bottomRight ?? null;
    }
}

export function intersect(quadTree1: Node | null, quadTree2: Node | null): Node | null {
    if (quadTree1.isLeaf) return quadTree1.val ? quadTree1 : quadTree2;
    if (quadTree2.isLeaf) return quadTree2.val ? quadTree2 : quadTree1;
    const topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft);
    const topRight = intersect(quadTree1.topRight, quadTree2.topRight);
    const bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
    const bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight);
    if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf
        && topLeft.val === topRight.val && topRight.val === bottomLeft.val
        && bottomLeft.val === bottomRight.val) {
        return new Node(topLeft.val, true);
    }
    return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
}
