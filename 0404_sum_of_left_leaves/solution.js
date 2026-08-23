// LeetCode 0404 - Sum of Left Leaves
var sumOfLeftLeaves = function (root) {
    if (!root) return 0;
    let total = 0;
    if (root.left && !root.left.left && !root.left.right) {
        total += root.left.val;
    } else {
        total += sumOfLeftLeaves(root.left);
    }
    total += sumOfLeftLeaves(root.right);
    return total;
};

module.exports = { sumOfLeftLeaves };
