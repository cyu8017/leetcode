// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

export class Node {
    val: string;
    left: Node | null;
    right: Node | null;

    constructor(val: string, left: Node | null = null, right: Node | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    evaluate(): number {
        if (!"+-*/".includes(this.val)) return Number(this.val);
        const a = this.left!.evaluate();
        const b = this.right!.evaluate();
        if (this.val === "+") return a + b;
        if (this.val === "-") return a - b;
        if (this.val === "*") return a * b;
        return Math.trunc(a / b);
    }
}

export class TreeBuilder {
    expTree(postfix: string[]): Node {
        const stack: Node[] = [];
        for (const token of postfix) {
            const node = new Node(token);
            if ("+-*/".includes(token)) {
                node.right = stack.pop()!;
                node.left = stack.pop()!;
            }
            stack.push(node);
        }
        return stack[stack.length - 1];
    }
}

function expTree(postfix: string[]): number {
    return new TreeBuilder().expTree(postfix).evaluate();
}
