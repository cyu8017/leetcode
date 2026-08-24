// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/


#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn game_result(mut head: Option<Box<ListNode>>) -> String {
        let mut odd = 0;
        let mut even = 0;
        while let Some(node) = head {
            let a = node.val;
            let next = node.next.unwrap();
            let b = next.val;
            if a < b {
                odd += 1;
            }
            if a > b {
                even += 1;
            }
            head = next.next;
        }
        if odd > even {
            "Odd".to_string()
        } else if odd < even {
            "Even".to_string()
        } else {
            "Tie".to_string()
        }
    }
}
