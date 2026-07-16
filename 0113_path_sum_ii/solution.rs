use std::cell::RefCell; use std::rc::Rc;
#[derive(Debug, PartialEq, Eq)] pub struct TreeNode { pub val:i32, pub left:Option<Rc<RefCell<TreeNode>>>, pub right:Option<Rc<RefCell<TreeNode>>> }
impl TreeNode { pub fn new(val:i32)->Self { Self { val,left:None,right:None } } }
impl Solution { pub fn path_sum(root:Option<Rc<RefCell<TreeNode>>>, target:i32)->Vec<Vec<i32>> {
    fn dfs(n:Option<Rc<RefCell<TreeNode>>>, sum:i32, path:&mut Vec<i32>, out:&mut Vec<Vec<i32>>) {
        if let Some(n)=n { let n=n.borrow(); path.push(n.val); let left=n.left.clone(); let right=n.right.clone();
            if left.is_none()&&right.is_none()&&sum==n.val { out.push(path.clone()); } else { dfs(left,sum-n.val,path,out); dfs(right,sum-n.val,path,out); } path.pop(); }
    } let mut out=vec![]; dfs(root,target,&mut vec![],&mut out); out
} }