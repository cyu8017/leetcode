// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

/**
 * @param {string} val
 * @param {Node|null} left
 * @param {Node|null} right
 */
function Node(val, left, right) {
    this.val = val === undefined ? " " : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * @param {string} s
 * @return {Node}
 */
var expTree = function(s) {
    const nodes = [];
    const ops = [];
    const priority = { "+": 1, "-": 1, "*": 2, "/": 2 };
    const apply = () => {
        const op = ops.pop();
        const right = nodes.pop();
        const left = nodes.pop();
        nodes.push(new Node(op, left, right));
    };
    for (const ch of s) {
        if (ch >= "0" && ch <= "9") {
            nodes.push(new Node(ch));
        } else if (ch === "(") {
            ops.push(ch);
        } else if (ch === ")") {
            while (ops[ops.length - 1] !== "(") apply();
            ops.pop();
        } else {
            while (ops.length && ops[ops.length - 1] !== "(" && priority[ops[ops.length - 1]] >= priority[ch]) {
                apply();
            }
            ops.push(ch);
        }
    }
    while (ops.length) apply();
    return nodes[0];
};
