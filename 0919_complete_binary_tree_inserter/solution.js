// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

function listToTree(values) {
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

function treeToList(root) {
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

class CBTInserter {
    /**
     * @param {TreeNode|number[]} root
     */
    constructor(root) {
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

    /**
     * @param {number} val
     * @return {number}
     */
    insert(val) {
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

    /**
     * @return {TreeNode}
     */
    getRoot() {
        return this.root;
    }

    /**
     * Local harness / Python-style alias.
     * @return {number[]}
     */
    get_root() {
        return treeToList(this.root);
    }
}

module.exports = { CBTInserter };
