// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

class Node {
    constructor(val = null, children = null) {
        this.val = val;
        this.children = children ?? [];
    }
}

class Codec {
    encode(root) {
        if (!root) return "";
        const parts = [];
        const queue = [root];
        while (queue.length > 0) {
            const node = queue.shift();
            parts.push(String(node.val));
            parts.push(String(node.children.length));
            for (const child of node.children) {
                parts.push(String(child.val));
                queue.push(child);
            }
        }
        return parts.join(",");
    }

    decode(data) {
        if (!data) return null;
        const values = data.split(",");
        let index = 0;

        const readRoot = () => {
            const value = Number(values[index]);
            const childCount = Number(values[index + 1]);
            index += 2;
            const node = new Node(value, []);
            for (let i = 0; i < childCount; i += 1) {
                node.children.push(new Node(Number(values[index]), []));
                index += 1;
            }
            return node;
        };

        const root = readRoot();
        const queue = [...root.children];
        while (queue.length > 0) {
            const node = queue.shift();
            const value = Number(values[index]);
            const childCount = Number(values[index + 1]);
            index += 2;
            if (value !== node.val) {
                throw new Error(`expected node value ${node.val}, found ${value}`);
            }
            for (let i = 0; i < childCount; i += 1) {
                const child = new Node(Number(values[index]), []);
                node.children.push(child);
                queue.push(child);
                index += 1;
            }
        }
        return root;
    }

    serialize(root) {
        return this.encode(root);
    }

    deserialize(data) {
        return this.decode(data);
    }
}

module.exports = { Codec, Node };
