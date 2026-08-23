// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

class Codec {
    serialize(root) {
        const parts = [];
        const preorder = (node) => {
            if (!node) {
                parts.push("#");
                return;
            }
            parts.push(String(node.val));
            preorder(node.left);
            preorder(node.right);
        };
        preorder(root);
        return parts.join(",");
    }

    deserialize(data) {
        if (!data) return null;
        const values = data.split(",");
        let index = 0;

        const build = () => {
            const token = values[index];
            index += 1;
            if (token === "#") return null;
            const node = { val: Number(token), left: null, right: null };
            node.left = build();
            node.right = build();
            return node;
        };

        return build();
    }
}

module.exports = { Codec };
