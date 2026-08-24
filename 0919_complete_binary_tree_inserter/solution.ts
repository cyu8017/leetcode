// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

function TreeNode(val: any, left: any, right: any): any {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}
function listToTree(values: any): any {
    if (!values || values.length === 0) return null;
    const root = new TreeNode(values[0]);
    const queue = [root];
    let i = 1;
    while (queue.length > 0 && i < values.length) {
        const node = queue.shift();
        if (i < values.length) {
            if (values[i] !== null && values[i] !== undefined) {
                node.left = new TreeNode(values[i]);
                queue.push(node.left);
            }
            i++;
        }
        if (i < values.length) {
            if (values[i] !== null && values[i] !== undefined) {
                node.right = new TreeNode(values[i]);
                queue.push(node.right);
            }
            i++;
        }
    }
    return root;
}
function treeToList(root: any): any {
    if (!root) return [];
    const result = [];
    const queue = [root];
    while (queue.length) {
        const node = queue.shift();
        if (!node) {
            result.push(null);
            continue;
        }
        result.push(node.val);
        if (node.left || node.right) {
            queue.push(node.left);
            queue.push(node.right);
        }
    }
    while (result.length && result[result.length - 1] === null) result.pop();
    return result;
}
export class CBTInserter {
    constructor(root: any) {
        if (Array.isArray(root)) root = listToTree(root);
        this.root = root;
        this.parents = [];
        const q = [root];
        while (q.length) {
            const node = q.shift();
            if (node.left !== null) q.push(node.left);
            else {
                this.parents.push(node);
                break;
            }
            if (node.right !== null) q.push(node.right);
            else {
                this.parents.push(node);
                break;
            }
        }
        while (q.length) this.parents.push(q.shift());
    }

    insert(val: any): any {
        const parent = this.parents[0];
        const child = new TreeNode(val);
        if (parent.left === null) parent.left = child;
        else {
            parent.right = child;
            this.parents.shift();
        }
        this.parents.push(child);
        return parent.val;
    }

    getRoot(): any {
        return this.root;
    }

    get_root(): any {
        return treeToList(this.root);
    }
}
