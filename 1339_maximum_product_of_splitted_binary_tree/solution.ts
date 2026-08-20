// LeetCode 1339 - Maximum Product Of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

function maxProduct(root: any): number {
    const sums: any[] = [];
    const total = (node: any): any => {
        if (!node) return 0;
        const value = node.val + total(node.left) + total(node.right);
        sums.push(value);
        return value;
    };
    const whole = total(root);
    let best = 0;
    for (const value of sums) best = Math.max(best, value * (whole - value));
    return best % 1000000007;
}
