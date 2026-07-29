// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    struct Node {
        int val;
        Node* next;
        Node(int v = 0) : val(v), next(nullptr) {}
    };

    Node* dummy_;
    int size_;

public:
    MyLinkedList() : dummy_(new Node()), size_(0) {}

    int get(int index) {
        if (index < 0 || index >= size_) {
            return -1;
        }
        Node* node = dummy_->next;
        for (int i = 0; i < index; ++i) {
            node = node->next;
        }
        return node->val;
    }

    void addAtHead(int val) { addAtIndex(0, val); }

    void addAtTail(int val) { addAtIndex(size_, val); }

    void addAtIndex(int index, int val) {
        if (index < 0 || index > size_) {
            return;
        }
        Node* prev = dummy_;
        for (int i = 0; i < index; ++i) {
            prev = prev->next;
        }
        Node* node = new Node(val);
        node->next = prev->next;
        prev->next = node;
        ++size_;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= size_) {
            return;
        }
        Node* prev = dummy_;
        for (int i = 0; i < index; ++i) {
            prev = prev->next;
        }
        Node* doomed = prev->next;
        prev->next = doomed->next;
        delete doomed;
        --size_;
    }
};
