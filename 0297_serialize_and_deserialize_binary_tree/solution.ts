// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export class Codec {
    serialize(root: TreeNode | null): string {
        if (!root) {
            return "";
        }
        const values: string[] = [];
        const queue: (TreeNode | null)[] = [root];
        while (queue.length > 0) {
            const node = queue.shift() as TreeNode | null;
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

    deserialize(data: string): TreeNode | null {
        if (!data) {
            return null;
        }
        const values = data.split(",");
        const root = new TreeNode(parseInt(values[0], 10));
        const queue: TreeNode[] = [root];
        let index = 1;
        while (queue.length > 0 && index < values.length) {
            const node = queue.shift() as TreeNode;
            if (index < values.length && values[index]) {
                node.left = new TreeNode(parseInt(values[index], 10));
                queue.push(node.left);
            }
            index += 1;
            if (index < values.length && values[index]) {
                node.right = new TreeNode(parseInt(values[index], 10));
                queue.push(node.right);
            }
            index += 1;
        }
        return root;
    }
}
