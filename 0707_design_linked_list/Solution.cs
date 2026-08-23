// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

public class MyLinkedList {
    private class Node {
        public int val;
        public Node next;
        public Node(int v = 0) { val = v; }
    }

    private readonly Node dummy = new Node();
    private int size;

    public MyLinkedList() { }

    public int Get(int index) {
        if (index < 0 || index >= size) return -1;
        Node node = dummy.next;
        for (int i = 0; i < index; i++) node = node.next;
        return node.val;
    }

    public void AddAtHead(int val) => AddAtIndex(0, val);
    public void AddAtTail(int val) => AddAtIndex(size, val);

    public void AddAtIndex(int index, int val) {
        if (index < 0 || index > size) return;
        Node prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;
        Node node = new Node(val) { next = prev.next };
        prev.next = node;
        size++;
    }

    public void DeleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        Node prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;
        prev.next = prev.next.next;
        size--;
    }
}
