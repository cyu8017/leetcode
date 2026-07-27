// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

/**
 * @param {Object|string} root1
 * @param {Object|string} root2
 * @return {boolean}
 */
var checkEquivalence = function(root1, root2) {
    function parse(data) {
        if (typeof data !== "string") return data;
        const inner = data.trim().replace(/^\[|\]$/g, "");
        const vals = inner ? inner.split(",") : [];
        const nodes = vals.map((x) => (x === "null" ? null : { val: x, left: null, right: null }));
        let k = 1;
        for (const node of nodes) {
            if (node) {
                if (k < nodes.length) node.left = nodes[k++];
                if (k < nodes.length) node.right = nodes[k++];
            }
        }
        return nodes[0] || null;
    }
    function count(node, out) {
        if (!node) return;
        if (node.val === "+") {
            count(node.left, out);
            count(node.right, out);
        } else {
            out[node.val] = (out[node.val] || 0) + 1;
        }
    }
    const a = {}, b = {};
    count(parse(root1), a);
    count(parse(root2), b);
    const keys = new Set([...Object.keys(a), ...Object.keys(b)]);
    for (const k of keys) if ((a[k] || 0) !== (b[k] || 0)) return false;
    return true;
};
