// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

using System.Collections.Generic;

public class Solution {
    public int NumComponents(ListNode head, int[] nums) {
        var present = new HashSet<int>(nums);
        int count = 0;
        bool connected = false;
        while (head != null) {
            if (present.Contains(head.val)) {
                if (!connected) { count++; connected = true; }
            } else connected = false;
            head = head.next;
        }
        return count;
    }
}
