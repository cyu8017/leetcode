// LeetCode 0116 - Populating Next Right Pointers in Each Node
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Node {
    val: number;
    left: Node | null;
    right: Node | null;
    next: Node | null;

    constructor(val?: number, left?: Node | null, right?: Node | null, next?: Node | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
        this.next = next ?? null;
    }
}

export function connect(root: Node | null): Node | null {
    if (!root) {
        return root;
    }

    let level: Node[] = [root];
    while (level.length) {
        for (let index = 0; index < level.length; index++) {
            level[index].next = index + 1 < level.length ? level[index + 1] : null;
        }
        const nextLevel: Node[] = [];
        for (const node of level) {
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        level = nextLevel;
    }
    return root;
}