// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    private static class Node {
        int val;
        Node next;
        Node(int v) { val = v; }
    }

    private final Node dummy = new Node(0);
    private int size;

    public MyLinkedList() {}

    public int get(int index) {
        if (index < 0 || index >= size) return -1;
        Node node = dummy.next;
        for (int i = 0; i < index; i++) node = node.next;
        return node.val;
    }

    public void addAtHead(int val) { addAtIndex(0, val); }

    public void addAtTail(int val) { addAtIndex(size, val); }

    public void addAtIndex(int index, int val) {
        if (index < 0 || index > size) return;
        Node prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;
        Node node = new Node(val);
        node.next = prev.next;
        prev.next = node;
        size++;
    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        Node prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;
        prev.next = prev.next.next;
        size--;
    }
}
