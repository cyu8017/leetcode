// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

using System.Collections.Generic;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode FrequenciesOfElements(ListNode head) {
        var cnt = new Dictionary<int, int>();
        for (; head != null; head = head.next) {
            if (!cnt.ContainsKey(head.val)) cnt[head.val] = 0;
            cnt[head.val]++;
        }
        ListNode dummy = new ListNode();
        foreach (var kv in cnt) {
            dummy.next = new ListNode(kv.Value, dummy.next);
        }
        return dummy.next;
    }
}
