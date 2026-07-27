// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

interface ExprNode {
    val: string;
    left: ExprNode | null;
    right: ExprNode | null;
}

function checkEquivalence(root1: ExprNode | string | null, root2: ExprNode | string | null): boolean {
    function parse(data: ExprNode | string | null): ExprNode | null {
        if (typeof data !== "string") return data;
        const inner = data.trim().replace(/^\[|\]$/g, "");
        const vals = inner ? inner.split(",") : [];
        const nodes: (ExprNode | null)[] = vals.map((x) =>
            x === "null" ? null : { val: x, left: null, right: null },
        );
        let k = 1;
        for (const node of nodes) {
            if (node) {
                if (k < nodes.length) node.left = nodes[k++];
                if (k < nodes.length) node.right = nodes[k++];
            }
        }
        return nodes[0] || null;
    }
    function count(node: ExprNode | null, out: Record<string, number>): void {
        if (!node) return;
        if (node.val === "+") {
            count(node.left, out);
            count(node.right, out);
        } else {
            out[node.val] = (out[node.val] || 0) + 1;
        }
    }
    const a: Record<string, number> = {}, b: Record<string, number> = {};
    count(parse(root1), a);
    count(parse(root2), b);
    const keys = new Set([...Object.keys(a), ...Object.keys(b)]);
    for (const k of keys) if ((a[k] || 0) !== (b[k] || 0)) return false;
    return true;
}
