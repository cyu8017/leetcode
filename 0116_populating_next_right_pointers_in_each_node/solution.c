// LeetCode 0116 - Populating Next Right Pointers in Each Node
struct Node { int val; struct Node *left,*right,*next; };
struct Node* connect(struct Node* root) {
    if (!root) return 0;
    root->next = 0;
    for (struct Node* level = root; level;) {
        struct Node dummy = {0, 0, 0, 0}, *tail = &dummy;
        for (struct Node* n = level; n; n = n->next) {
            if (n->left) tail = tail->next = n->left;
            if (n->right) tail = tail->next = n->right;
        }
        level = dummy.next;
    }
    return root;
}