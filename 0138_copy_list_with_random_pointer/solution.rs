// LeetCode 0138 - Copy List with Random Pointer
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug)]
pub struct Node { pub val: i32, pub next: Option<Rc<RefCell<Node>>>, pub random: Option<Rc<RefCell<Node>>> }
impl Node { pub fn new(val: i32) -> Self { Self { val, next: None, random: None } } }
impl Solution {
    pub fn copy_random_list(head: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
        fn clone(node: Rc<RefCell<Node>>, copies: &mut HashMap<usize, Rc<RefCell<Node>>>) -> Rc<RefCell<Node>> {
            let key = Rc::as_ptr(&node) as usize;
            if let Some(copy) = copies.get(&key) { return copy.clone(); }
            let copy = Rc::new(RefCell::new(Node::new(node.borrow().val)));
            copies.insert(key, copy.clone());
            let (next, random) = { let n = node.borrow(); (n.next.clone(), n.random.clone()) };
            copy.borrow_mut().next = next.map(|n| clone(n, copies));
            copy.borrow_mut().random = random.map(|n| clone(n, copies));
            copy
        }
        head.map(|node| clone(node, &mut HashMap::new()))
    }
}