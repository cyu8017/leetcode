using System.Collections.Generic;

public class TreeNode
{
    public int Val;
    public TreeNode Left;
    public TreeNode Right;

    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        Val = val;
        Left = left;
        Right = right;
    }
}

public class BSTIterator
{
    private readonly Stack<TreeNode> _stack = new Stack<TreeNode>();

    public BSTIterator(TreeNode root)
    {
        PushLeft(root);
    }

    public int Next()
    {
        var node = _stack.Pop();
        PushLeft(node.Right);
        return node.Val;
    }

    public bool HasNext()
    {
        return _stack.Count > 0;
    }

    private void PushLeft(TreeNode node)
    {
        while (node != null)
        {
            _stack.Push(node);
            node = node.Left;
        }
    }
}
