// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
function removeDuplicates(s) {
    const stack = [];
    for (const ch of s) {
        if (stack.length && stack[stack.length - 1] === ch)
            stack.pop();
        else
            stack.push(ch);
    }
    return stack.join('');
}
