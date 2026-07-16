// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

export class Node {
    val: number | null;
    children: Node[];

    constructor(val: number | null = null, children: Node[] | null = null) {
        this.val = val;
        this.children = children ?? [];
    }
}

export class Codec {
    encode(root: Node | null): string {
        if (!root) return "";
        const parts: string[] = [];
        const queue: Node[] = [root];
        while (queue.length > 0) {
            const node = queue.shift() as Node;
            parts.push(String(node.val));
            parts.push(String(node.children.length));
            for (const child of node.children) {
                parts.push(String(child.val));
                queue.push(child);
            }
        }
        return parts.join(",");
    }

    decode(data: string): Node | null {
        if (!data) return null;
        const values = data.split(",");
        let index = 0;

        const readRoot = (): Node => {
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
            const node = queue.shift() as Node;
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

    serialize(root: Node | null): string {
        return this.encode(root);
    }

    deserialize(data: string): Node | null {
        return this.decode(data);
    }
}
