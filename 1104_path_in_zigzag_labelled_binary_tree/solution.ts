// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

function pathInZigZagTree(label: number): number[] {
    const path = [label];
    while (label > 1) {
        const level = Math.floor(Math.log2(label));
        label >>= 1;
        label = (1 << level) - 1 - label + (1 << (level - 1));
        path.push(label);
    }
    return path.reverse();
}
