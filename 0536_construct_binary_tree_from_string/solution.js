// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    str2tree(s) {
        if (!s) return null;

        let index = 0;
        const parse = () => {
            if (index >= s.length) return null;

            let sign = 1;
            if (s[index] === "-") {
                sign = -1;
                index += 1;
            }

            let value = 0;
            while (index < s.length && s[index] >= "0" && s[index] <= "9") {
                value = value * 10 + Number(s[index]);
                index += 1;
            }

            const node = new TreeNode(sign * value);

            if (index < s.length && s[index] === "(") {
                index += 1;
                node.left = parse();
                index += 1;
            }

            if (index < s.length && s[index] === "(") {
                index += 1;
                node.right = parse();
                index += 1;
            }

            return node;
        };

        return parse();
    }
}

module.exports = { Solution, TreeNode };
