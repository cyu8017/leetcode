// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

function removeDuplicates(s: string, k: number): string {
    const stack = [];
    for (const ch of s) {
        if (stack.length && stack[stack.length - 1][0] === ch) stack[stack.length - 1][1]++;
        else stack.push([ch, 1]);
        if (stack[stack.length - 1][1] === k) stack.pop();
    }
    return stack.map(([ch, count]) => ch.repeat(count)).join('');
}
