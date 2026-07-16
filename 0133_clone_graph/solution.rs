// LeetCode 0133 - Clone Graph
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug)]
pub struct Node { pub val: i32, pub neighbors: Vec<Rc<RefCell<Node>>> }
impl Node { pub fn new(val: i32) -> Self { Self { val, neighbors: Vec::new() } } }
impl Solution {
    pub fn clone_graph(node: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
        fn dfs(node: Rc<RefCell<Node>>, copies: &mut HashMap<usize, Rc<RefCell<Node>>>) -> Rc<RefCell<Node>> {
            let key = Rc::as_ptr(&node) as usize;
            if let Some(copy) = copies.get(&key) { return copy.clone(); }
            let copy = Rc::new(RefCell::new(Node::new(node.borrow().val)));
            copies.insert(key, copy.clone());
            let neighbors = node.borrow().neighbors.clone();
            copy.borrow_mut().neighbors = neighbors.into_iter().map(|n| dfs(n, copies)).collect();
            copy
        }
        node.map(|n| dfs(n, &mut HashMap::new()))
    }
}