// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class Codec {
    /**
     * @param {TreeNode|null} root
     * @return {string}
     */
    serialize(root) {
        if (!root) {
            return "";
        }
        const values = [];
        const queue = [root];
        while (queue.length > 0) {
            const node = queue.shift();
            if (node) {
                values.push(String(node.val));
                queue.push(node.left);
                queue.push(node.right);
            } else {
                values.push("");
            }
        }
        while (values.length > 0 && values[values.length - 1] === "") {
            values.pop();
        }
        return values.join(",");
    }

    /**
     * @param {string} data
     * @return {TreeNode|null}
     */
    deserialize(data) {
        if (!data) {
            return null;
        }
        const values = data.split(",");
        const root = { val: parseInt(values[0], 10), left: null, right: null };
        const queue = [root];
        let index = 1;
        while (queue.length > 0 && index < values.length) {
            const node = queue.shift();
            if (index < values.length && values[index]) {
                node.left = { val: parseInt(values[index], 10), left: null, right: null };
                queue.push(node.left);
            }
            index += 1;
            if (index < values.length && values[index]) {
                node.right = { val: parseInt(values[index], 10), left: null, right: null };
                queue.push(node.right);
            }
            index += 1;
        }
        return root;
    }
}

module.exports = { Codec };
