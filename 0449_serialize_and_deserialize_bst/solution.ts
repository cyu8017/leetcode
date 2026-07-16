// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

export class Codec {
    serialize(root: TreeNode | null): string {
        const parts: string[] = [];
        const preorder = (node: TreeNode | null): void => {
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

    deserialize(data: string): TreeNode | null {
        if (!data) return null;
        const values = data.split(",");
        let index = 0;

        const build = (): TreeNode | null => {
            const token = values[index];
            index += 1;
            if (token === "#") return null;
            const node = new TreeNode(Number(token));
            node.left = build();
            node.right = build();
            return node;
        };

        return build();
    }
}
