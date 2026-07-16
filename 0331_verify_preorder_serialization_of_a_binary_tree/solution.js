// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree
var isValidSerialization = function(preorder) {
    let slots = 1;
    for (const node of preorder.split(",")) {
        slots -= 1;
        if (slots < 0) return false;
        if (node !== "#") slots += 2;
    }
    return slots === 0;
};
