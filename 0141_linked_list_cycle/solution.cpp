struct ListNode{int val;ListNode*next;};class Solution{public:bool hasCycle(ListNode*h){ListNode*s=h,*f=h;while(f&&f->next){s=s->next;f=f->next->next;if(s==f)return true;}return false;}};
