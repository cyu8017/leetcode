// LeetCode 1305 - All Elements In Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

function getAllElements(root1: any, root2: any): number[] {
    const inorder = (root: any): any => {
        if (!root) return [];
        return [...inorder(root.left), root.val, ...inorder(root.right)];
    };
    const a = inorder(root1), b = inorder(root2);
    const answer: any[] = [];
    let i = 0, j = 0;
    while (i < a.length || j < b.length) {
        if (j === b.length || (i < a.length && a[i] <= b[j])) answer.push(a[i++]);
        else answer.push(b[j++]);
    }
    return answer;
}
