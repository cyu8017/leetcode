use std::cell::RefCell; use std::rc::Rc;
#[derive(Debug, PartialEq, Eq)] pub struct TreeNode { pub val:i32, pub left:Option<Rc<RefCell<TreeNode>>>, pub right:Option<Rc<RefCell<TreeNode>>> }
impl TreeNode { pub fn new(val:i32)->Self { Self { val,left:None,right:None } } }
impl Solution { pub fn has_path_sum(root:Option<Rc<RefCell<TreeNode>>>, sum:i32)->bool {
    match root { None=>false, Some(n)=>{ let n=n.borrow(); if n.left.is_none()&&n.right.is_none(){n.val==sum}else{Self::has_path_sum(n.left.clone(),sum-n.val)||Self::has_path_sum(n.right.clone(),sum-n.val)} } }
} }