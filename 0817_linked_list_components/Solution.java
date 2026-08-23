// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

import java.util.*;

class Solution {
    public int numComponents(ListNode head, int[] nums) {
        Set<Integer> present = new HashSet<>();
        for (int x : nums) present.add(x);
        int count = 0;
        boolean connected = false;
        while (head != null) {
            if (present.contains(head.val)) {
                if (!connected) {
                    count++;
                    connected = true;
                }
            } else {
                connected = false;
            }
            head = head.next;
        }
        return count;
    }
}
