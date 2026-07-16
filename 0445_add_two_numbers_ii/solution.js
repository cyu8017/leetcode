// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

class Solution {
    addTwoNumbers(l1, l2) {
        const stack1 = [];
        const stack2 = [];
        while (l1) {
            stack1.push(l1.val);
            l1 = l1.next;
        }
        while (l2) {
            stack2.push(l2.val);
            l2 = l2.next;
        }

        let carry = 0;
        let head = null;
        while (stack1.length > 0 || stack2.length > 0 || carry) {
            let total = carry;
            if (stack1.length > 0) total += stack1.pop();
            if (stack2.length > 0) total += stack2.pop();
            carry = Math.floor(total / 10);
            const digit = total % 10;
            head = { val: digit, next: head };
        }
        return head;
    }
}

module.exports = { Solution };
